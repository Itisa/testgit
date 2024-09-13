import socket

from config import *

def udp_client(server_host='127.0.0.1', server_port=34227):
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:
		message = "Hello, UDP server!"

		client_socket.sendto(message.encode(), (server_host, server_port))

		data, server = client_socket.recvfrom(1024)
		print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
	udp_client(host,port)