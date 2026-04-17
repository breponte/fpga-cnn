import transmit
import data_loader

from pathlib import Path
import time
import yaml
import numpy as np
import math

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "../data/cifar-10-batches-py"
CONFIGS_DIR = BASE_DIR / "configs.yaml"

def load_yaml_config(path):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config

if __name__ == "__main__":
    config = load_yaml_config(CONFIGS_DIR)

    client_socket, client_address = \
        transmit.start_server(      # block until connection established
            config.get("host"),
            config.get("port")
        )
    
    data_loader.download_dataset()
    
    # flatten all data batches into one large dataset
    data = []
    labels = []
    for batch_i in range(config.get("batch_count")):
        batch_file = DATA_DIR / f"data_batch_{batch_i + 1}"
        data_i, labels_i = data_loader.unpickle(batch_file)
        data.append(data_i)
        labels.append(labels_i)
    
    data = np.stack(data, axis=0).reshape(
        -1, config.get("num_channels"), config.get("image_width"), config.get("image_width")
    )
    labels = np.stack(labels, axis=0).reshape(-1)

    start_time = time.time()

    transmit.send_data(client_socket, data.tobytes())    # ignore labels, FPGA won't initially
    messages = []
    for _ in range(math.ceil(config.get("total_images") / config.get("images_per_recv"))):
        message = transmit.receive_data(
            client_socket,
            config.get("images_per_recv"),
            config.get("num_channels"),
            config.get("image_width")
        )
        message_np = np.frombuffer(message, np.dtype("uint8")).reshape((
            -1,
            config.get("num_channels"),
            config.get("image_width"),
            config.get("image_width"))
        )
        messages.append(message_np)

    end_time = time.time()

    round_trip_time = (end_time - start_time) * 1000  # in milliseconds

    messages = np.vstack(messages).reshape(
        (-1, config.get("num_channels"), config.get("image_width"), config.get("image_width"))
    )
    print(f"Matches: {np.all(messages == data)}")
    print(f"Round-trip time: {round_trip_time:.3f} ms")        

    transmit.close_connection(client_socket)