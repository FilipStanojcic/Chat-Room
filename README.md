# Description
Client-server communication program using TCP sockets. Programs are run and used in command line arguments.
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

# Execution
Download Server.py and Client.py to your device. In a command terminal (Windows CMD, Powershell, Terminal, etc.)
navigate to downloads using the "cd" command (for example: C:\User\fstan> cd Downloads) or wherever the files
have been saved. Run the server file using "python Server.py". In another terminal, run the client file using
"python Client.py". Now, the server and client can communicate, just input a message into the client terminal
(mentioned above) and the server will act accordingly.

# Difficulties
Running the exit command early in coding caused an error in server execution resulting in a stall and severing
communication. Proper error handling caught the error allowing for a clean disconnect between server and client.

# Future Improvements
Client reconnection is based on which client disconnected first instead of the lowest available number.

If ever properly implemented, a network such as this would need user-login/password requirements for security.
