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

    s.connect((config.get("host"), config.get("port")))     # check if host is open, fail otherwise
    
    try:
        if (image_size * config.get("images_per_recv") > 65536):
            raise ValueError(
                f"Image size * Images per recv exceed 65536: {image_size * images_per_recv}"
            )

        data = []
        count = 0
        num_minibatches = math.ceil(config.get("total_images") / config.get("images_per_recv"))
        while count < num_minibatches:
            message = b""
            images_per_minibatch = min(
                config.get("images_per_recv"),
                config.get("total_images") - count * config.get("images_per_recv")
            )
            while len(message) < image_size * images_per_minibatch:
                chunk = s.recv(
                    min(
                        image_size * images_per_minibatch,
                        image_size * images_per_minibatch - len(message)
                    )
                )
                if not chunk:
                    break
                message += chunk

            if not message:
                break

            message_np = np.frombuffer(message, np.dtype("uint8")).reshape((
                -1,
                config.get("num_channels"),
                config.get("image_width"),
                config.get("image_width"))
            )
            data.append(message_np)
            count += 1
        
        data = np.vstack(data).reshape(-1, 3, 32, 32)

        # feedforward images into CNN
        model = torch.hub.load(
            "chenyaofo/pytorch-cifar-models",
            "cifar10_resnet20",
            pretrained=True
        )
        model.eval()
        with torch.no_grad():
            out = model(data)

        s.sendall(out.tobytes())     # echo the message back to the client

    except Exception as e:
        print(f"Error handling client: {e}")
        s.close()