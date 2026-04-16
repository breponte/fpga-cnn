import transmit
import data_loader

from pathlib import Path
import time
import numpy as np

BATCH_COUNT = 5
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data/cifar-10-batches-py"
HOST = '127.0.0.1'
PORT = 5000
NUM_CHANNELS = 3
WIDTH = 32

if __name__ == "__main__":
    client_socket, client_address = \
        transmit.start_server(HOST, PORT)   # block until connection established
    
    data_loader.download_dataset()
    
    # flatten all data batches into one large dataset
    data = []
    labels = []
    for batch_i in range(BATCH_COUNT):
        batch_file = DATA_DIR / f"data_batch_{batch_i + 1}"
        data_i, labels_i = data_loader.unpickle(batch_file)
        data.append(data_i)
        labels.append(labels_i)
    
    data = np.stack(data, axis=0).reshape(-1, NUM_CHANNELS, WIDTH, WIDTH)
    labels = np.stack(labels, axis=0).reshape(-1)

    start_time = time.time()

    transmit.send_data(client_socket, data.tobytes())    # ignore labels, FPGA won't initially
    messages = []
    for _ in range(data.shape[0]):
        message = transmit.receive_data(client_socket)
        message_np = np.frombuffer(message, np.dtype("uint8"))
        messages.append(message_np)

    end_time = time.time()

    round_trip_time = (end_time - start_time) * 1000  # in milliseconds

    messages = np.stack(messages, axis=0).reshape((-1, NUM_CHANNELS, WIDTH, WIDTH))
    print(f"Matches: {np.all(messages == data)}")
    print(f"Round-trip time: {round_trip_time:.3f} ms")        

    transmit.close_connection(client_socket)