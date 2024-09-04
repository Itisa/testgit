import socket  

from config import *

def udp_client(server_host='127.0.0.1', server_port=34227):  
    # 创建一个socket对象  
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client_socket:  
        # 要发送的数据  
        message = "Hello, UDP server!"  
  
        # 发送数据报  
        client_socket.sendto(message.encode(), (server_host, server_port))  
  
        # 接收来自服务器的响应（如果需要的话）  
        data, server = client_socket.recvfrom(1024)  
        print(f"Received from server: {data.decode()}")  
  
if __name__ == "__main__":  
    udp_client(host,port)