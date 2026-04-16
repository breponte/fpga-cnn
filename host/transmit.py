"""
transmit.py

Set up server on host and transmits data from the host to the FPGA board.
"""

import socket

MAX_BYTES_RECV = 65536

def start_server(host, port):
    """
    Starts the server using IPv4 and TCP protocol and listens for
    client connections.
    Args:
        host: The host address to listen on.
        port: The port to listen on.
    Returns:
        client_socket: The socket object for the client connection.
        client_address: The address of the client connection.
    """
    server = socket.socket(
        socket.AF_INET,      # use IPv4 addresses
        socket.SOCK_STREAM   # use TCP streams
    )
    
    server.setsockopt(       # enable reuse of the address/port
        socket.SOL_SOCKET,
        socket.SO_REUSEADDR,
        1
    )

    server.bind((host, port))
    server.listen(1)
    # print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server.accept()
        server.close()
        return client_socket, client_address

def send_data(client_socket, data):
    """
    Sends data to the client.
    Args:
        client_socket: The socket object for the client connection.
        data: The data to send to the client.
    """
    client_socket.sendall(data)

def receive_data(client_socket):
    """
    Receives data from the client. Receives up to the specified MAX_BYTES_RECV
    Args:
        client_socket: The socket object for the client connection.
    """
    try:
        message = client_socket.recv(3*32*32)
        return message

    except Exception as e:
        print(f"Error handling client: {e}")
        client_socket.close()

def close_connection(client_socket):
    """
    Closes the client connection.
    Args:
        client_socket: The socket object for the client connection.
    """
    client_socket.close()