"""
Thomas Carlucci
CS 166 OL
Cat Coin Blockchain
"""
import csv


def menu_loop() -> int:
    option = 0

    print("Please select from the following options:")
    print("1: Check Wallet Balance")
    print("2: Transfer CatCoins")
    print("3: Quit CatCoin")

    while not option:
        try:
            option = int(input(">>>"))
            if option < 1 or option > 3:
                print("Please choose a valid option!")
                option = 0
            else:
                return option
        except ValueError:
            print("Please enter a valid integer!")


def load_blockchain() -> dict:
    d = {}
    with open('wallets.csv', mode='r') as f:
        csvFile = csv.reader(f)
        for lines in csvFile:
            d[int(lines[0])] = int(lines[1])

    return d


if __name__ == "__main__":
    print("Welcome to CatCoin!")
    blockchain_info = load_blockchain()
    quit_flag = False

    while not quit_flag:
        choice = menu_loop()
        if choice == 1:
            wallet = 0
            while not wallet:
                try:
                    wallet = int(input("Please select the wallet whose balance you'd like to view. 1, 2, or 3:"))
                    if wallet < 1 or wallet > 3:
                        print("Please choose a valid wallet!")
                        wallet = 0
                    else:
                        print("===============================")
                        print("Wallet " + str(wallet) + " balance: " + str(blockchain_info[wallet]) + " CatCoins")
                        print("===============================")
                except ValueError:
                    print("Please enter a valid integer!")

        elif choice == 2:
            source = 0
            destination = 0
            while not source:
                try:
                    source = int(input("Please choose a source wallet: 1, 2, or 3:"))
                    if source < 1 or source > 3:
                        print("Please choose a valid wallet!")
                        source = 0
                except ValueError:
                    print("Please enter a valid integer!")
            while not destination:
                try:
                    destination = int(input("Please choose a source wallet: 1, 2, or 3:"))
                    if destination < 1 or destination > 3:
                        print("Please choose a valid wallet!")
                        destination = 0
                    elif destination == source:
                        print("Destination wallet cannot be source wallet")
                        destination = 0
                except ValueError:
                    print("Please enter a valid integer!")
        else:
            quit_confirmation = ""
            while not quit_confirmation:
                quit_confirmation = input("Are you sure you want to exit CatCoin? y/n")
                if quit_confirmation == "y" or quit_confirmation == "Y":
                    exit()
                elif quit_confirmation == "n" or quit_confirmation == "N":
                    pass
                else:
                    print("Please enter a valid value, y/n")
                    quit_confirmation = ""
