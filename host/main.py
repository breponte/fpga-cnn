import transmit
import data_loader

from pathlib import Path
import time

BATCH_COUNT = 5
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data/cifar-10-batches-py"

if __name__ == "__main__":
    # host = '127.0.0.1'
    # port = 5000
    # message = b"Hello, world"

    # client_socket, client_address = \
    #     transmit.start_server(host, port)   # block until connection established
    
    data_loader.download_dataset()
    
    for batch_i in range(BATCH_COUNT):
        batch_file = DATA_DIR / f"data_batch_{batch_i + 1}"
        data_np, labels_np = data_loader.unpickle(batch_file)
        print(data_np.shape)
        print(labels_np.shape)

    # for _ in range(10):
    #     start_time = time.time()
    #     transmit.send_data(client_socket, message)
    #     data = transmit.receive_data(client_socket)
    #     end_time = time.time()

    #     round_trip_time = (end_time - start_time) * 1000  # in milliseconds

    #     print(f"Received: {data.decode('utf-8')}")
    #     print(f"Round-trip time: {round_trip_time:.3f} ms")

    # transmit.close_connection(client_socket)