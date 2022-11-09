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
    print(menu_loop())

