import socket  

from config import *

def tcp_client(host='127.0.0.1', port=34226):  
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
	client_socket.connect((host, port))  
  
	try:  
		message = input("Enter message: ")  
		while message.lower().strip() != 'bye':  
			client_socket.sendall(message.encode())  
			data = client_socket.recv(1024)  
			print(f"Received from server: {data.decode()}")  
			message = input("Enter message: ")  
	finally:  
		client_socket.close()  
  
if __name__ == "__main__":  
	tcp_client(host,port)