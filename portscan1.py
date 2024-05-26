#!/usr/bin/python

import socket

host = '127.0.0.1'
port_https = 443


def portscanner(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host, port))
    if result == 0:
        print(f'Port {port} ouvert')
    else:
        print(f'Port {port} fermé')
    sock.close()


portscanner(port_https)
