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

def show_menu():
    print(banner)

    print("Select a vulnerability scanner category:\n")

    for number, category in categories.items():
        print(f"{number}. {category}")

    print("0. exit")

def show_scanner():
    print("Select what to run:\n")

    for number, categories in categories_web.items():
        print(f"{number}. {categories}")

    print("0. Return")

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

        print(f"\n[+] Selected category: {category}")

        web_scanners = [...]
        # api_scanners = [...]
        #
        show_scanner(category)

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()