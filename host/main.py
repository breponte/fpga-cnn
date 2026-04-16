import transmit
import data_loader

from pathlib import Path
import time
import numpy as np

BATCH_COUNT = 5
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data/cifar-10-batches-py"

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000

    client_socket, client_address = \
        transmit.start_server(host, port)   # block until connection established
    
    data_loader.download_dataset()
    
    for batch_i in range(BATCH_COUNT):
        batch_file = DATA_DIR / f"data_batch_{batch_i + 1}"
        data_np, labels_np = data_loader.unpickle(batch_file)

        start_time = time.time()
        transmit.send_data(client_socket, data_np[0].tobytes())    # ignore labels, FPGA won't initially
        data = transmit.receive_data(client_socket)
        end_time = time.time()

        round_trip_time = (end_time - start_time) * 1000  # in milliseconds

        data = np.frombuffer(data, np.dtype("uint8")).reshape((3, 32, 32))
        print(f"Matches: {np.all(data == data_np[0])}")
        print(f"Round-trip time: {round_trip_time:.3f} ms")        

    transmit.close_connection(client_socket)