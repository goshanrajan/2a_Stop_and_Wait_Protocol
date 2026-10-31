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
