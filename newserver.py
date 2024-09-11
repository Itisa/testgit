import socket
import threading
from config import *

def handle_client(client_socket):
    try:
        # 接收账号
        client_socket.send(b"Username: ")
        username = client_socket.recv(1024).decode().strip()

        # 接收密码
        client_socket.send(b"Password: ")
        password = client_socket.recv(1024).decode().strip()

        # 认证
        if username in users and users[username] == password:
            client_socket.send(b"Login successful!\n")
        else:
            client_socket.send(b"Login failed!\n")
            client_socket.close()
            return

        while True:
            msg = client_socket.recv(1024).decode().strip()
            if msg.lower() == "exit":
                client_socket.send(b"Goodbye!")
                break
            else:
                client_socket.send(msg.encode())

    except Exception as e:
        print(f"Error: {e}")

    finally:
        client_socket.close()

def start_server(host='127.0.0.1', port=9999):
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host, port))
    server.listen(5)
    print(f"[*] Listening on {host}:{port}")

    while True:
        client_socket, addr = server.accept()
        print(f"[*] Accepted connection from {addr}")
        
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server(host,port)