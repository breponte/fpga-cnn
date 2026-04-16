"""
test_client.py

Test the client-server connection on local host.
Is not referenced in main.py and is intended to be run as a standalone script.
"""

import socket
import numpy as np

HOST = '127.0.0.1'
PORT = 5000
NUM_CHANNELS = 3
WIDTH = 32
IMAGE_SIZE = NUM_CHANNELS * WIDTH * WIDTH
IMAGES_PER_RECV = 1

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))     # check if host is open, fail otherwise
    
    try:
        data = []
        count = 0
        while count < 50000:
            message = b""
            while len(message) < IMAGE_SIZE * IMAGES_PER_RECV:
                chunk = s.recv(
                    min(
                        IMAGE_SIZE * IMAGES_PER_RECV,
                        IMAGE_SIZE * IMAGES_PER_RECV - len(message)
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