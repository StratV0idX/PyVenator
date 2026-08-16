import sys, time
import socket, threading

class web:
    def __init__ (self):
        self.port_starting = int(input("Enter port to start search"))
        self.port_ending = int(input("Enter port upto search"))
        self.s = socket.socket()
        self.ip = socket.gethostbyname()

    def port_scanner(s, ip, port_starting, port_ending, r=1):
        open_ports = []
        for j in range(port_starting, port_ending):
            port = port+j
            print(port)
        def check_ports():
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

        for i in range(port_starting, port_ending):
            thread = threading.Thread(target=check_ports(ip, port))
            
    