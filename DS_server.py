import socket, threading
from datetime import datetime as dt

HOST = '127.0.0.1' 
PORT = 65433 
def handle_client(conn, addr): # runs in its own thread per client
    print(f"[NEW] {addr} connected.")
    with conn:
        while True:
            data = conn.recv(1024) # wait for a message
            if not data: # empty = client disconnected
                break
            msg = data.decode()
            print(f"[{addr}] {msg} || SERVER TIME : {dt.now().strftime('%Y/%m/%d | %I:%M %p')} ||")
            if msg.upper() == "EXIT": # client asked to end the session
                break
    conn.sendall(f"Echo: {msg}".encode()) # reply to only this client

    print(f"[CLOSED] {addr}")

def start_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print(f"Listening on {HOST}:{PORT}")
    while True:
        conn, addr = s.accept() # wait for the next client
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    start_server()