import socket

from config import *

def udp_server(host='127.0.0.1', port=34227):
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
		server_socket.bind((host, port))
		print(f"Server is listening on {host}:{port}")

		while True:
			data, addr = server_socket.recvfrom(1024)
			print(f"Received message: {data.decode()} from {addr}")

			response = "Received"
			server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
	udp_server(host,port)