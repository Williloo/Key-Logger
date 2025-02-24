import socket
import time

HOST = '' 	## Leave Blank
PORT = 65535

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))

    while True:
        s.listen()
        conn, addr = s.accept()
        f = open(f'LOG_{addr[0]}', "a")
        with conn:
            print('Connected by', addr)
            while True:
                data = conn.recv(1024)
                if not data:
                    f.close()
                    print('Disconnected by', addr)
                    break
                f.write(f'{time.ctime()}'+str(data)+'\n')
