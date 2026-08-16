import sys, time
import socket, threading

class web:
    def __init__ (self):
        self.port = int(input("Enter the port to search"))
        self.s = socket.socket()
        self.ip = socket.gethostbyname()

    def port_scanner(s, ip, port):
        open_ports = []
        for i in range(1, port):
            print (i)
    