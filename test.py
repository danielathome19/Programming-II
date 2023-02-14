import threading
import socket
import rsa

public_key, private_key = rsa.newkeys(1024)  # 1024 is the key length (bits)
public_partner = None
DEFAULT_IP_PORT = ("127.0.0.1", 1234)
choice = input("Do you want to be the server or client? (s/c): ")

if choice == "s":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(DEFAULT_IP_PORT)
    server.listen()
    print("Waiting for connection...")
    client, addr = server.accept()
    print("Connected to", addr)
    client.send(public_key.save_pkcs1("PEM"))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    print("Hit 'Ctrl+C' to exit at any time.")
elif choice == "c":
    print("Connecting to server...", end="")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(DEFAULT_IP_PORT)
    print("success! Connected to " + str(client.getpeername()))
    public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
    client.send(public_key.save_pkcs1("PEM"))
    print("Hit 'Ctrl+C' to exit at any time.")
else:
    exit()

def sendMsg(c):
    while True:
        msg = input()
        print('\033[1A' + '\033[K', end='')
        c.send(rsa.encrypt(msg.encode(), public_partner))
        print("\033[91mYou: \033[0m" + msg)

def recvMsg(c):
    while True:
        try:
            msg = rsa.decrypt(c.recv(1024), private_key)
            print("\033[94mPartner: \033[0m" + msg.decode())
        except:
            print("Partner has disconnected. Press enter to exit.")
            exit()

try:
  send_thread = threading.Thread(target=sendMsg, args=(client,)).start()
  recv_thread = threading.Thread(target=recvMsg, args=(client,)).start()
except: pass