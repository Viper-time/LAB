import socket
import threading

# Function to run the server
def run_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345
    server_socket.bind((host, port))
    server_socket.listen(1)
    print("Server is listening...")

    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")

    # Receive data from the client
    data = conn.recv(1024).decode()
    print(f"Server received: {data}")

    # Send response to the client
    conn.send("Hello, Client!".encode())
    conn.close()

# Function to run the client
def run_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = 'localhost'
    port = 12345

    client_socket.connect((host, port))

    # Send data to the server
    client_socket.send("Hello, Server!".encode())

    # Receive response from the server
    response = client_socket.recv(1024).decode()
    print(f"Client received: {response}")
    client_socket.close()

# Run server and client using threading
server_thread = threading.Thread(target=run_server)
client_thread = threading.Thread(target=run_client)

server_thread.start()
client_thread.start()

server_thread.join()
client_thread.join()
