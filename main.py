"""
Thomas Carlucci
CS 166 OL
Cat Coin Blockchain
"""

import csv
import miner
from datetime import datetime as t


def menu_loop() -> int:
    """
    Collect menu option from user consisting of:
    1: Checking the balance of a wallet
    2: Transferring coins between two wallets
    3: Exiting the program

    :return: option: int
    """
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


def load_wallets() -> dict:
    """
    Loads wallet info from wallets.csv

    :return: wallets: dict
    """

    wallets = {}
    with open('wallets.csv', mode='r') as f:
        wallet_data = csv.reader(f)
        for lines in wallet_data:
            wallets[float(lines[0])] = float(lines[1])

    return wallets


def add_to_blockchain(fr, to, amt):
    prev_block = []
    with open("blocks.csv", mode="r") as bc:
        blox = csv.reader(bc)
        for lines in blox:
            prev_block = lines

    nonce, timestamp = miner.mining(prev_block[-1])
    block = [fr, to, amt, int(lines[3]) + 1, prev_block[-1], timestamp, prev_block[-1], nonce]
    block_string = ""
    for i in range(1, len(block)-2):
        block_string += str(block[i]) + ","
    block_string += str(block[len(block)-1])

    with open("blocks.csv", mode="a") as bc:
        bc.writelines("\n"+block_string)

if __name__ == "__main__":
    print("Welcome to CatCoin!")
    wallets_info = load_wallets()
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
                        print("Wallet " + str(wallet) + " balance: " + str(wallets_info[wallet]) + " CatCoins")
                        print("===============================")
                except ValueError:
                    print("Please enter a valid integer!")

        elif choice == 2:
            source = 0
            destination = 0
            transfer_amt = 0
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
            while not transfer_amt:
                try:
                    transfer_amt = float(input("Enter the amount you wish to transfer:"))
                    if transfer_amt <= 0:
                        print("Please enter a valid float value!")
                        transfer_amt = 0
                    elif transfer_amt > wallets_info[source]:
                        print("Transfer amount exceeds wallet " + str(source) + "'s balance!")
                        transfer_amt = 0
                except ValueError:
                    print("Please enter a valid float value!")

            # TODO: Add miner functionality
            confirm_transfer = ""
            while not confirm_transfer:
                confirm_transfer = input("Are you sure you want to transfer " + str(transfer_amt) +
                                         " CatCoin? y/n")
                if confirm_transfer == "y" or confirm_transfer == "Y":
                    wallets_info[source] = wallets_info[source] - transfer_amt
                    wallets_info[destination] = wallets_info[destination] + transfer_amt

                    with open('wallets.csv', mode='w') as f:
                        for i in range(len(wallets_info)):
                            f.writelines(str(i+1) + "," + str(wallets_info[i+1]))
                            f.writelines("\n")

                    add_to_blockchain(source, destination, transfer_amt)

                    print("=====================")
                    print("Transaction Complete!")
                    print("=====================")
                elif confirm_transfer == "n" or confirm_transfer == "N":
                    print("======================")
                    print("Transaction Cancelled.")
                    print("======================")
                else:
                    print("Please enter a valid value, y/n")
                    confirm_transfer = ""
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
