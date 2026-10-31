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
