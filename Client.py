"""
-------------------------------------------------------
[TCP Echo Communication, Client.py file]
-------------------------------------------------------
__updated__ = "2025-03-27"
-------------------------------------------------------
"""
# Imports
import socket

def start_client():
    """
    -------------------------------------------------------
    Connects to TCP server and handles sending and receiving
    messages.
    -------------------------------------------------------
    Parameters:
        N/A
    Returns:
        N/A
    ------------------------------------------------------
    """
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))  # Connect to the server
    data = client_socket.recv(1024).decode()
    print(data)
    if data == "Server is full. Try again later.":
        client_socket.close()
        return

    while True:
        message = input(
            "Enter message to send (enter 'exit' to close connection): ")
        client_socket.send(message.encode())

        # Receive data in a loop until the entire message is received
        response = ""
        while True:
            # Adjust buffer size if needed
            part = client_socket.recv(4096).decode()
            response += part
            if len(part) < 4096:  # Assuming no more data is coming
                break

        if response.strip() == "close":
            print("Connection closed by server.")
            break
        else:
            print(f"Received from server:\n{response}")

    client_socket.close()

if __name__ == '__main__':
    start_client()
