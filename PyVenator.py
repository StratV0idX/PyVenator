banner = r"""
+===============================================================================================+

|'########::'##:::'##:'##::::'##:'########:'##::: ##::::'###::::'########::'#######::'########::|
| ##.... ##:. ##:'##:: ##:::: ##: ##.....:: ###:: ##:::'## ##:::... ##..::'##.... ##: ##.... ##:|
| ##:::: ##::. ####::: ##:::: ##: ##::::::: ####: ##::'##:. ##::::: ##:::: ##:::: ##: ##:::: ##:|
| ########::::. ##:::: ##:::: ##: ######::: ## ## ##:'##:::. ##:::: ##:::: ##:::: ##: ########::|
| ##.....:::::: ##::::. ##:: ##:: ##...:::: ##. ####: #########:::: ##:::: ##:::: ##: ##.. ##:::|
| ##::::::::::: ##:::::. ## ##::: ##::::::: ##:. ###: ##.... ##:::: ##:::: ##:::: ##: ##::. ##::|
| ##::::::::::: ##::::::. ###:::: ########: ##::. ##: ##:::: ##:::: ##::::. #######:: ##:::. ##:|
|..::::::::::::..::::::::...:::::........::..::::..::..:::::..:::::..::::::.......:::..:::::..::|

+===============================================================================================+
"""
print(banner)

categories = {
    1: "web",
    2: "api",
    3: "network",
    4: "cms",
    5: "dns",
    6: "ssl_tls",
    7: "cloud",
    8: "container",
    9: "source_code",
    10: "dependency",
}

scanners = {
    "web": {
        1: "Port_Scanner",
        2: "Web_Crawler",
        3: "Header_Scanner",
    },

    "api": {
        1: "API_Endpoint_Scanner",
        2: "API_Configuration_Checker",
    },

    "network": {
        1: "Service_Enumerator",
        2: "Network_Configuration_Checker",
    },

    "cms": {
        1: "CMS_Enumerator",
    },

    "dns": {
        1: "DNS_Configuration_Checker",
    },

    "ssl_tls": {
        1: "TLS_Configuration_Checker",
    },

    "cloud": {
        1: "Cloud_Configuration_Checker",
    },

    "container": {
        1: "Container_Configuration_Checker",
    },

    "source_code": {
        1: "SAST_Scanner",
    },

    "dependency": {
        1: "Dependency_Vulnerability_Checker",
    },
}

def show_scanner(category):
    print(f"\n[{category.upper()} SCANNERS]\n")

    category_scanners = scanners.get(category, {})

    if not category_scanners:
        print("No scanners available.")
        return

    for number, scanner in category_scanners.items():
        print(f"{number}. {scanner}")

    print("0. Return")
    
def show_menu():

    print("Select a vulnerability scanner category:\n")

    for number, scanner in categories.items():
        print(f"{number}. {scanner}")

    print("0. exit")

def main():
    while True:
        show_menu()

        choice = input("\n> ").strip()

        if choice == "0":
            print("Exiting...")
            break

        try:
            category = categories[int(choice)]
        except (ValueError, KeyError):
            print("\n[!] Invalid option.")
            input("Press Enter to continue...")
            continue

        while True:
            show_scanner(category)

            scanner_choice = input("\n> ").strip()

            if scanner_choice == "0":
                break

            try:
                scanner = scanners[category][int(scanner_choice)]
            except (ValueError, KeyError):
                print("\n[!] Invalid scanner.")
                input("Press Enter to continue...")
                continue

            print(f"\n[+] Selected: {scanner}")

            # Run the selected scanner here.
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
