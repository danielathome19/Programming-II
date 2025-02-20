import rsa  # pip install rsa
import socket
import threading

public_key, private_key = rsa.newkeys(1024)  # 1024 bits (1kb)
DEFAULT_IP_PORT = ("127.0.0.1", 9999)
choice = input("Do you want to be server or client? (s/c): ")

if choice == "s":  # Server
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # TCP connection
    server.bind(DEFAULT_IP_PORT)
    server.listen()
    print("Waiting for connection...")
    client, addr = server.accept()
    print("Connected to", addr)
    client.send(public_key.save_pkcs1())
    partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    print("Use 'Ctrl+C' to disconnect.")
elif choice == "c":  # Client
    print("Connecting to server...", end='')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(DEFAULT_IP_PORT)
    print("success! Connected to", client.getpeername())
    partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1())
    print("Use 'Ctrl+C' to disconnect.")
else: exit()

def send_msg(c):
    while True:
        try:
            msg = input()
            print('\033[A' + '\033[K', end='')  # Delete input line
            c.send(rsa.encrypt(msg.encode(), partner))
            print("\033[91mYou: \033[0m" + msg)
        except: exit()

def recv_msg(c):
    while True:
        try:
            msg = rsa.decrypt(c.recv(1024), private_key)
            print("\033[94mPartner: \033[0m" + msg.decode())
        except:
            print("Partner has disconnected. Exiting...")
            exit()

try:
    send_thread = threading.Thread(target=send_msg, args=(client,)).start()
    recv_thread = threading.Thread(target=recv_msg, args=(client,)).start()
except: pass
