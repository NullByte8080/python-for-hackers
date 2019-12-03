import socket
import sys

def create_socket():
    try:
        global host
        global port
        global s

        host = ""
        port = 4444
        s = socket.socket()
    except socket.error as msg:
        print(str(msg))

def bind_socket():
    try:
        global host
        global port
        global s

        print("binding on port:" + str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print(str(msg) + "retrieving connection.......")
        bind_socket()

def accept_conn():
    conn, add = s.accept()
    print("receiving connection from :" + "IP" + str(add[0]) + "port" + str(add[1]))
    send_commands(conn)
    conn.close()

def send_commands(conn):
    while True:
        cmd = input()
        if cmd == 'quite':
            conn.close()
            s.close()
            sys.exit()

        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))

        responce = str(conn.recv(1024), "utf-8")

        print(responce, end = "")

def main():
    create_socket()
    bind_socket()
    accept_conn()

main()
