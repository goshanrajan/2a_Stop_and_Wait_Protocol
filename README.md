# 2a_Stop_and_Wait_Protocol
## AIM 
To write a python program to perform stop and wait protocol
## ALGORITHM
1. Start the program.
2. Get the frame size from the user
3. To create the frame based on the user request.
4. To send frames to server from the client side.
5. If your frames reach the server it will send ACK signal to client
6. Stop the Program
## PROGRAM
Developed by : T.GOSHANRAJAN (212225040098)

### Client
```python
import socket

HOST = 'localhost'
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
    client_socket.connect((HOST, PORT))
    print("Connected to server.")

    while True:
        data = client_socket.recv(1024)
        if not data:
            print("Server disconnected.")
            break

        message = data.decode()
        print(f"Server: {message}")

        if message.lower() == 'quit':
            break

        reply = input("Enter a reply: ")
        if not reply:
            continue

        client_socket.sendall(reply.encode())
        if reply.lower() == 'quit':
            break

```
### Server
```python
import socket

HOST = 'localhost'
PORT = 8001

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = server_socket.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            message = input("Enter a message to send (or 'quit' to exit): ")
            if not message:
                continue

            conn.sendall(message.encode())
            if message.lower() == 'quit':
                break

            data = conn.recv(1024)
            if not data:
                break

            print(f"Client: {data.decode()}")

```
## OUTPUT
Refer to the screenshot below to see the program's output.
<img width="1282" height="290" alt="Screenshot 2026-10-31 142013" src="https://github.com/user-attachments/assets/ae72f3bc-b361-4b09-a336-068a7f8ed42a" />
<img width="1287" height="266" alt="Screenshot 2026-10-31 142039" src="https://github.com/user-attachments/assets/05bd00c4-6ea8-4420-b768-689a5a95f041" />


## RESULT
Thus, python program to perform stop and wait protocol was successfully executed.

