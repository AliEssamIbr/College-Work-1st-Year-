import socket
HOST, PORT = '127.0.0.1', 65433

def start_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    while True:
        msg = input("Message (EXIT to quit): ")
        s.sendall(msg.encode())
        if msg.upper() == "EXIT":
            break
        print("Server:", s.recv(1024).decode())
    s.close()

if __name__ == "__main__":
    start_client()