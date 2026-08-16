import sys, time
import socket, threading

class web:
    def __init__ (self):
        self.port = int(input("Enter the port to search"))
        self.s = socket.socket()
        self.ip = socket.gethostbyname()

    def port_scanner(s, ip, port, r=1):
        open_ports = []
        try:
            s.socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            r = s.connect_ex((ip, port))
            if r == 0:
                con = f"Port{port} is open"
                print(con)
            s.close()


        except Exception as e:
            pass

        for i in range(1, port):
            print (i)
    