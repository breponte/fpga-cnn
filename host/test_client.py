"""
test_client.py

Test the client-server connection on local host.
Is not referenced in main.py and is intended to be run as a standalone script.
"""

import socket
import numpy as np
import yaml
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
CONFIGS_DIR = BASE_DIR / "configs.yaml"

def load_yaml_config(path):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    config = load_yaml_config(CONFIGS_DIR)
    image_size = config.get("num_channels") * config.get("image_width") * config.get("image_width")

    s.connect((config.get("host"), config.get("port")))     # check if host is open, fail otherwise
    
    try:
        data = []
        count = 0
        while count < 50000:
            message = b""
            while len(message) < image_size * config.get("images_per_recv"):
                chunk = s.recv(
                    min(
                        image_size * config.get("images_per_recv"),
                        image_size * config.get("images_per_recv") - len(message)
                    )
                )
                if not chunk:
                    break
                message += chunk

            if not message:
                break

            message_np = np.frombuffer(message, np.dtype("uint8")).reshape((3, 32, 32))
            data.append(message_np)
            count += 1
            
        data = np.stack(data, axis=0).reshape(-1, 3, 32, 32)
        print(data.shape)
        s.sendall(data.tobytes())     # echo the message back to the client

    except Exception as e:
        print(f"Error handling client: {e}")
        s.close()