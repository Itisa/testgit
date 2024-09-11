import socket

from config import *

def udp_server(host='127.0.0.1', port=34227):
	# 创建一个socket对象
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server_socket:
		# 绑定地址和端口
		server_socket.bind((host, port))
		print(f"Server is listening on {host}:{port}")

		while True:
			# 接收数据报
			data, addr = server_socket.recvfrom(1024)
			print(f"Received message: {data.decode()} from {addr}")

			# 处理数据（这里只是简单地打印出来

			# 可以选择发送响应给客户端
			response = "Received"
			server_socket.sendto(response.encode(), addr)

if __name__ == "__main__":
	udp_server(host,port)