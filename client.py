import socket

# Configurer le serveur
HOST = '0.0.0.0'  # Écoute sur toutes les interfaces réseau
PORT = 12345       # Port d'écoute

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    server_socket.bind((HOST, PORT))
    server_socket.listen()
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, client_address = server_socket.accept()
        with client_socket:
            print(f"Connection from {client_address}")
            client_socket.sendall(b"Hello, client! Type your message.\n")
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break
                print(f"Received: {data.decode()}")
                client_socket.sendall(b"Echo: " + data)
