import socket
import threading
import time

from config import *

def udp_client(server_host='127.0.0.1', server_port=9999, timeout=5):
	# 创建一个socket对象
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	# 要发送的数据
	message = "Hello, UDP server!".encode()

	# 发送数据报
	client_socket.sendto(message, (server_host, server_port))

	# 创建一个超时定时器
	def timeout_handler():
		time.sleep(timeout)
		if client_socket:
			print(f"Timeout: No response from server after {timeout} seconds.")
			client_socket.close()

	timeout_thread = threading.Thread(target=timeout_handler)
	timeout_thread.start()

	try:
		# 尝试接收来自服务器的响应，但设置一个内部超时（通过线程）
		data, server = client_socket.recvfrom(1024)
		print(f"Received from server: {data.decode()}")
	except socket.timeout:
		# 注意：这个异常通常不会在UDP中直接触发，因为UDP没有内置的超时机制
		# 但如果你的环境或库修改了socket行为，可能会用到
		print("Socket timeout occurred, but this is not typical for UDP.")
	finally:
		# 无论是否超时，都尝试关闭socket
		if client_socket:
			client_socket.close()
		# 停止定时器线程（如果它还没有执行到关闭socket）
		if timeout_thread.is_alive():
			timeout_thread.join(0)# 尝试立即停止线程，但注意这不会强制停止

if __name__ == "__main__":
	udp_client(host,port)

# 注意：上面的代码实际上并没有真正地在UDP socket上设置超时，
# 而是通过另一个线程来实现了一个“软”超时。如果UDP socket接收到了数据，
# 那么它将正常处理并忽略超时线程。如果没有接收到数据并且超时了，
# 那么超时线程将关闭socket并打印一条消息。