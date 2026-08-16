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


def show_menu():
    print(banner)

    print("Select a vulnerability scanner category:\n")

    for number, category in categories.items():
        print(f"{number}. {category}")

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

        print(f"\n[+] Selected category: {category}")

        # This is where you can load the scanners
        # belonging to that category.
        #
        # Example:
        #
        # web_scanners = [...]
        # api_scanners = [...]
        #
        # show_scanners(category)

        input("\nPress Enter to return to the menu...")


if __name__ == "__main__":
    main()