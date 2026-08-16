import socket


def port_scanner():
    target = input("Enter target hostname/IP: ").strip()
    start_port = int(input("Enter starting port: "))
    end_port = int(input("Enter ending port: "))
    name = {
        20: "FTP (File Transfer Protocol)",
        21: "FTP (File Transfer Protocol)",
        22: "SSH (Secure Shell)",
        23: "Telnet",
        25: "SMTP (Simple Mail Transfer Protocol)",
        53: "DNS (Domain Name System)",
        67: "DHCP (Dynamic Host Configuration Protocol)",
        68: "DHCP (Dynamic Host Configuration Protocol)",
        80: "HTTP (Hypertext Transfer Protocol)",
        110: "POP3 (Post Office Protocol version 3)",
        123: "NTP (Network Time Protocol)",
        143: "IMAP (Internet Message Access Protocol)",
        161: "SNMP (Simple Network Management Protocol)",
        162: "SNMP (Simple Network Management Protocol)",
        443: "HTTPS (Hypertext Transfer Protocol Secure)",
        445: "SMB (Server Message Block)",
        3389: "RDP (Remote Desktop Protocol)"
    }
    
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
            print(f"[+] Port {port} : {name} is OPEN")
            open_ports.append(port)

    print("\n[+] Scan complete.")

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print(f"[+] Open ports: {open_ports}")