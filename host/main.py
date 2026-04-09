import transmit

import time

if __name__ == "__main__":
    host = '127.0.0.1'
    port = 5000
    message = b"Hello, world"

    client_socket, client_address = \
        transmit.start_server(host, port)   # block until connection established
    
    for _ in range(10):
        start_time = time.time()
        transmit.send_data(client_socket, message)
        data = transmit.receive_data(client_socket)
        end_time = time.time()

        round_trip_time = (end_time - start_time) * 1000  # in milliseconds

        print(f"Received: {data.decode('utf-8')}")
        print(f"Round-trip time: {round_trip_time:.3f} ms")

    transmit.close_connection(client_socket)