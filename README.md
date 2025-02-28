# Description
Client-server communication program using TCP sockets.
Socket, threading, json, and datetime libraries are used.

A maximum of three clients can connect at the same time, and a lock is implemented to ensure thread safety.
Each connected client is assigned a unique name in the format "Client0X" X=(1,2,3).

Each client's address, connection times and disconnection times are stored. Clients can request the status
of all connected clients using the "status" command, which sends back the in-memory cache of clients.

Clients can exit by sending the "exit" command, which updates their disconnection time and frees their ID
for reuse.

Clients can send messages to the opened server, which will respond back with the repeated message + " ACK".
When the maximum number of clients is reached, new connections are informed and close immediately upon any 
attempt to connect.

# Difficulties
Running the exit command early in coding caused an error in server execution resulting in a stall and severing
communication. Proper error handling caught the error allowing for a clean disconnect between server and client.

# Future Improvements
Client reconnection is based on which client disconnected first instead of the lowest available number.

If ever properly implemented, a network such as this would need user-login/password requirements for security.
