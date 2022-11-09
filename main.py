"""
Thomas Carlucci
CS 166 OL
Cat Coin Blockchain
"""

def menu_loop() -> int:
    ans = 0

    print("Please select from the following options:")
    print("1: Check Wallet Balance")
    print("2: Transfer CatCoins")
    print("3: Quit CatCoin")

    while ans == 0:
        try:
            option = int(input(">>>"))

            if option < 1 or option > 3:
                print("Please choose a valid wallet!")
            else:
                ans = option
        except ValueError:
            print("Please enter a valid integer!")

    return ans


if __name__ == "__main__":
    print("Welcome to CatCoin!")
    quit_flag = False
    while not quit_flag:
        option = menu_loop()

        if option == 1:
            pass
            # Option 1 stuff
        elif option == 2:
            pass
            # Option 2 stuff
        else:
            quit_confirmation = ""
            while not quit_confirmation:
                quit_confirmation = input("Are you sure you want to exit CatCoin? y/n")
                if quit_confirmation == "y" or quit_confirmation == "Y":
                    exit()
                elif quit_confirmation == "n" or quit_confirmation == "N":
                    quit_confirmation = "n"
                else:
                    print("Please enter a valid value, y/n")
                    quit_confirmation = ""


