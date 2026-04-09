"""
test_client.py

Test the client-server connection on local host.
Is not referenced in main.py and is intended to be run as a standalone script.
"""

import socket

HOST = '127.0.0.1'
PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))     # check if host is open, fail otherwise
    
    try:
        while True:
            message = s.recv(1024)

            if not message:
                break

            print(f"{message.decode('utf-8')}")
            
            s.send(message)     # echo the message back to the client
    except Exception as e:
        print(f"Error handling client: {e}")
        s.close()