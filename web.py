import socket


def port_scanner():
    target = input("Enter target hostname/IP: ").strip()
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))

    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Could not resolve target.")
        return

    print(f"\n[+] Scanning {target} ({ip})")
    print(f"[+] Ports: {start_port}-{end_port}\n")

    open_ports = []

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.7)

        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            print(f"[+] Port {port} is OPEN")
            open_ports.append(port)

    print("\n[+] Scan complete.")

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"[+] Open ports: {open_ports}")