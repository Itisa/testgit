import socket
import tkinter as tk
from tkinter import scrolledtext, messagebox, font
from config import *
class ClientApp:
	def __init__(self, root):
		self.root = root
		self.root.title("Socket Client")
		self.logged = False
		self.socket = None

		self.login_frame = tk.Frame(self.root)
		self.login_frame.pack(padx=10, pady=10)

		tk.Label(self.login_frame, text="Username:").grid(row=0, column=0, padx=5, pady=5)
		self.username_entry = tk.Entry(self.login_frame)
		self.username_entry.grid(row=0, column=1, padx=5, pady=5)

		tk.Label(self.login_frame, text="Password:").grid(row=1, column=0, padx=5, pady=5)
		self.password_entry = tk.Entry(self.login_frame, show="*")
		self.password_entry.grid(row=1, column=1, padx=5, pady=5)

		self.login_button = tk.Button(self.login_frame, text="Login", command=self.login)
		self.login_button.grid(row=2, columnspan=2, pady=10)

		self.chat_frame = tk.Frame(self.root)
		
		self.chat_text = scrolledtext.ScrolledText(self.chat_frame, state='disabled', wrap=tk.WORD,fg="#00f")
		self.chat_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
		self.chat_text.configure(bg="#39C5BB")
		
		self.message_entry = tk.Entry(self.chat_frame)
		self.message_entry.pack(padx=10, pady=10, fill=tk.X)
		
		self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
		self.send_button.pack(pady=10)

		self.root.bind("<Return>", self.on_enter_pressed)

	def on_enter_pressed(self,event):
		if self.logged:
			self.send_message()
		else:
			self.login()

	def connect(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.connect((host, port))

	def login(self):

		username = self.username_entry.get()
		password = self.password_entry.get()
		if username == "" or password == "":
			messagebox.showerror("Login Error","Not filled username or password")
			return 
		
		self.connect()
		response1 = self.socket.recv(1024).decode() # b"Username:"
		self.socket.send(username.encode())
		response2 = self.socket.recv(1024).decode() # b"Password:"
		self.socket.send(password.encode())

		response = self.socket.recv(1024).decode()
		
		if "Login successful!" in response:
			self.logged = True
			self.show_chat()
		else:
			messagebox.showerror("Login Failed", "Invalid username or password")
			self.socket.close()

	def show_chat(self):
		self.login_frame.pack_forget()
		self.chat_frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
		self.chat_text.config(state='normal')
		self.chat_text.insert(tk.END, "Login successful!\n")
		self.chat_text.config(state='disabled')

	def send_message(self):
		msg = self.message_entry.get()
		if msg.strip() == "":
			messagebox.showerror("Send Error","No message")
			return
		self.message_entry.delete(0, tk.END)
		
		self.chat_text.config(state='normal')
		self.chat_text.insert(tk.END, "send: "+msg + "\n")
		self.chat_text.config(state='disabled')

		self.socket.send(msg.encode())

		response = self.socket.recv(1024).decode()
		self.chat_text.config(state='normal')
		self.chat_text.insert(tk.END, "resp: "+response + "\n")
		self.chat_text.config(state='disabled')

		if msg.lower() == "exit":
			self.socket.close()
			self.root.quit()

if __name__ == "__main__":
	root = tk.Tk()
	app = ClientApp(root)
	root.mainloop()