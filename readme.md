# 一个简单的Socket连接的小东西

**注:请保证在当前文件夹下有一个config.py的文件，其中有**

<a id="appendix2"></a>

```python
host = "127.0.0.1" #服务器的ip地址
port = 12345 #服务器监听的端口
users = {    #可选，用于登录的账号密码，样例是默认的账号密码
	"user1": "password1",
	"user2": "password2"
}
```

## TCP连接



有两种server可供选择

* server.py 仅作为echo服务器，即时返回所有通过TCP发送过来的信息
* newserver.py 需要通过密码登录，格式见[此处](#appendix1)

有两种client可供选择

* client.py 只有命令行，通过命令行传输文字信息到服务器
* newclient.py 拥有可视化窗口，需要输入账号和密码，默认账号密码见[此处](#appendix2)



## UDP连接

server使用UDPserver.py

有两种client可供选择

* UDPclient.py 将数据报传到server，并接收所服务器发回的消息
* UDPclient_1.py 将数据报传到server，并接收所服务器发回的消息，同时有一个5秒的timeout，若超时后还没有接受到服务器的返回值会自动结束程序

<a id="appendix1"></a>

### 附录

1. 当TCP建立时会收到服务器发来的`Username: `，用户在上传用户名后会收到服务器发来的`Password: `，在上传密码后

   若账号密码正确：服务器返回`Login successful!`

   若账号密码错误：服务器返回`Login failed!`，同时关闭TCP连接

   



