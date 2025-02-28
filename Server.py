"""
-------------------------------------------------------
[TCP Echo Communication, Server.py file]
-------------------------------------------------------
__updated__ = "2025-02-28"
-------------------------------------------------------
"""
# Imports
import socket
import threading
import json
from datetime import datetime
# Constants
max_clients = 3
client_lock = threading.Lock()
clients = {}
available_ids = [f"Client{str(i).zfill(2)}" for i in range(
    1, max_clients + 1)]  # List of available IDs


def handle_client(client_socket, addr):
    """
    -------------------------------------------------------
    Handle a connected client.
    -------------------------------------------------------
    Parameters:
        client_socket:
        addr:
    Returns:
        N/A
    -------------------------------------------------------
    """
    global available_ids
    client_name = available_ids.pop(0)  # Get the next available client ID

    with client_lock:
        print(f"Connected to {client_name}")
        client_socket.send(f"You are {client_name}".encode())

        # If the client already exists, just append a new connection record
        if client_name not in clients:
            clients[client_name] = []

        # Add a new connection record
        clients[client_name].append({
            'address': addr,
            'connection_time': datetime.now().isoformat(),
            'disconnection_time': None
        })

    try:
        while True:
            data = client_socket.recv(1024).decode()
            lowcased_data = data.lower()
            if lowcased_data == "status":
                print("Received request for cache.")
                # Prepare the status output in the fixed order
                ordered_clients = {}
                for client_id in [f"Client{str(i).zfill(2)}" for i in range(1, max_clients + 1)]:
                    if client_id in clients:
                        ordered_clients[client_id] = clients[client_id]
                cache_info = json.dumps(ordered_clients, indent=4)
                client_socket.send(f"{cache_info}\n".encode())  # Add newline
            elif lowcased_data == "exit":
                print("Received request to close client connection.")
                # Record disconnection time for the last connection record
                clients[client_name][-1]['disconnection_time'] = datetime.now().isoformat()
                client_socket.send("close".encode())
                break
            else:
                print(f"Received: {data}")
                client_socket.send(f"{data} ACK".encode())

    except Exception as e:
        print(f"Error handling client {client_name}: {e}")
    finally:
        with client_lock:
            if client_name in clients:
                clients[client_name][-1]['disconnection_time'] = datetime.now().isoformat()
            # Re-add the client ID to available IDs
            available_ids.append(client_name)
            print(f"{client_name} disconnected and is now available for reuse.")
        client_socket.close()


def start_server():
    """
    -------------------------------------------------------
    Starts TCP server to initiate socket connection.
    -------------------------------------------------------
    Parameters:
        N/A
    Returns:
        N/A
    -------------------------------------------------------
    """
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind to localhost on port 12345
    server_socket.bind(('localhost', 12345))
    server_socket.listen()
    print("Server is listening...")

    while True:
        client_socket, addr = server_socket.accept()
        with client_lock:
            if len(available_ids) == 0:
                client_socket.send("Server is full. Try again later.".encode())
                client_socket.close()
            else:
                client_thread = threading.Thread(
                    target=handle_client, args=(client_socket, addr))
                client_thread.start()


if __name__ == '__main__':
    start_server()
