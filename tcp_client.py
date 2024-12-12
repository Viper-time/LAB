import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to the server.")
    client_socket.sendall(b'Hello, server! This is a TCP message.')
    data = client_socket.recv(1024)

print(f"Received back: {data.decode()}")
