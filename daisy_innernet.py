#!/usr/bin/python3

import socket
from _thread import *

host = ''
port = 5556

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host,port))
except socket.error as e:
    print(str(e))

s.listen(5) # how many concurrent connections

print('waiting for connection')

def threaded_client(conn):
    conn.send(str.encode('Echo test. Type somethin: '))

    while True:
        data = conn.recv(2048)
        print(data.decode('utf-8'))
        # This would be the handling of data sent from client
        reply = 'Server response: ' + data.decode('utf-8')
        if not data:
            break
        conn.sendall(str.encode(reply))
    conn.close()

# Accept connections and start threads
while True:
    conn, addr = s.accept()
    print('Connected to: ' + addr[0] + ':' + str(addr[1]))

    start_new_thread(threaded_client, (conn,)) 
