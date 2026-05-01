"""
test_client.py

Test the client-server connection on local host.
Is not referenced in main.py and is intended to be run as a standalone script.
"""

import socket
import numpy as np
import yaml
from pathlib import Path
import math
import torch

BASE_DIR = Path(__file__).resolve().parent
CONFIGS_DIR = BASE_DIR / "configs.yaml"

def load_yaml_config(path):
    with open(path, 'r') as file:
        config = yaml.safe_load(file)
    return config

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    config = load_yaml_config(CONFIGS_DIR)
    image_size = config.get("num_channels") * config.get("image_width") * config.get("image_width")
    batch_size = config.get("batch_size")
    total_images = config.get("total_images")

    s.connect((config.get("host"), config.get("port")))     # check if host is open, fail otherwise
    
    try:
        message = b""
        num_batches = math.ceil(config.get("total_images") / config.get("batch_size"))
        while len(message) < total_images * image_size:
            chunk = s.recv(
                # attempt to receive full message or receive what's left
                min(
                    batch_size * image_size,
                    total_images * image_size - len(message)
                )
            )
            if not chunk:
                break
            message += chunk
        
        data = np.frombuffer(message, np.dtype("uint8")).reshape((
            -1,
            config.get("num_channels"),
            config.get("image_width"),
            config.get("image_width")
        ))

        # feedforward images into CNN
        model = torch.hub.load(
            "chenyaofo/pytorch-cifar-models",
            "cifar10_resnet20",
            pretrained=True
        )
        model.eval()

        out = []
        mean = np.array([0.4914, 0.4822, 0.4465], dtype=np.float32)[:, None, None]
        std  = np.array([0.2470, 0.2435, 0.2616], dtype=np.float32)[:, None, None]
        for start in range(0, len(data), batch_size):
            batch = data[start:start + batch_size].astype(np.float32) / 255.0
            batch = (batch - mean) / std
            with torch.no_grad():
                y = model(torch.from_numpy(batch))
            out.append(y.numpy())

        out = np.vstack(out)
        s.sendall(out.tobytes())

    except Exception as e:
        print(f"Error handling client: {e}")
        s.close()