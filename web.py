import socket
import time


def port_scanner():

    port_common = {20, 21, 22, 23, 25, 53, 67, 68, 
                        69, 80, 110, 123, 143, 443, 445, 
                        587, 993, 995, 1433, 3306, 3389}

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
            1433: "Microsoft SQL Server",
            3306: "MySQL Database",
            3389: "RDP (Remote Desktop Protocol)"
        }
    
    target = input("Enter target hostname/IP: ").strip()
    port_choice = input("Do you want to search only common port ?  [Y/n]").strip().lower()
    if port_choice in ('y', 'yes'):
        ports = sorted(port_common)
        print("[+] Scanning common ports only.")

    elif port_choice in ("n", "no", ""):
        try:
            start_port = int(input("Enter starting port: "))
            end_port = int(input("Enter ending port: "))

            if start_port < 0 or end_port > 65535 or start_port > end_port:
                print("[!] Invalid port range.")
                return
        
            ports = range(start_port, end_port)

        except ValueError:
                    print("[!] Ports must be numbers.")
                    return
    else:
        print("[!] Please enter Y or n.")
        print(port_choice)
        return
    
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print("[!] Could not resolve target.")
        return

    total_ports = len(ports)
    open_ports = []

    start_time = time.time()

    print(f"\n[+] Scanning {target} ({ip})")
    print(f"[+] Ports: {start_port}-{end_port}\n")

    for index, port in enumerate(
        ports,
        start=1
    ):
        sock = socket.socket(
            socket.AF_INET,
            socket.SOCK_STREAM
        )

        sock.settimeout(0.7)

        try:
            result = sock.connect_ex((ip, port))
        except socket.error:
            result = 1
        finally:
            sock.close()

        if result == 0:
            service = name.get(port, "Unknown Service")

            # Clear the current progress line
            print("\r\033[K", end="")

            # Print the discovered port
            print(
                f"[+] Port {port:<5}: "
                f"{service} is OPEN"
            )

            open_ports.append(port)

        # -----------------------------
        # Progress calculation
        # -----------------------------

        elapsed = time.time() - start_time

        percentage = (
            index / total_ports
        ) * 100

        if elapsed > 0:
            scan_rate = index / elapsed
            remaining_ports = total_ports - index
            eta = remaining_ports / scan_rate
        else:
            eta = 0

        bar_length = 30

        completed = int(
            bar_length * index / total_ports
        )

        progress = (
            "#" * completed
            + "." * (bar_length - completed)
        )

        # Draw ONE progress line
        print(
            f"\r\033[K"
            f"[ + ] process:{progress} "
            f"{percentage:6.2f}% "
            f"| elapsed: {elapsed:6.1f}s "
            f"| ETA: {eta:6.1f}s "
            f"| open: {len(open_ports)}",
            end="",
            flush=True
        )
        
    print("\n")

    elapsed = time.time() - start_time

    print("=" * 70)
    print("[+] Scan complete")
    print(f"[+] Target       : {target}")
    print(f"[+] IP           : {ip}")
    print(f"[+] Ports scanned: {total_ports}")
    print(f"[+] Open ports   : {len(open_ports)}")
    print(f"[+] Time         : {elapsed:.2f}s")
    print("=" * 70)

    if not open_ports:
        print("[-] No open ports found.")
    else:
        print("\n[+] Open ports:")

        for port in open_ports:
            service = name.get(
                port,
                "Unknown Service"
            )

            print(
                f"    [OPEN] {port:<5} "
                f"{service}"
            )