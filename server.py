import socket  
import threading  

from config import *

def handle_client(client_socket, addr):  
	try:  
		print(f"Connected by {addr}")  
		while True:  
			data = client_socket.recv(1024)  
			if not data:  
				break  
			print(f"Received: {data.decode()}")  
			# Echo back the received data  
			client_socket.sendall(data)  
	except Exception as e:  
		print(f"Error handling client {addr}: {e}")  
	finally:  
		client_socket.close()  
		print(f"Disconnected by {addr}")  
  
def tcp_server(host='127.0.0.1', port=34226):  
	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  
	server_socket.bind((host, port))  
	server_socket.listen()  
	print(f"Server is listening on {host}:{port}")  
  
	try:  
		while True:  
			client_socket, addr = server_socket.accept()  
			# Create a new thread to handle the client  
			client_thread = threading.Thread(target=handle_client, args=(client_socket, addr))  
			client_thread.start()  
	except KeyboardInterrupt:  
		print("Server is shutting down...")  
	except Exception as e:  
		print(f"Server error: {e}")  
	finally:  
		server_socket.close()  
  
if __name__ == "__main__":  
	tcp_server(host,port)