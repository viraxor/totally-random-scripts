from random import randint
from time import sleep
from secrets import token_hex
from colorama import Fore
from os.path import exists
from requests import get

def mine(amnt):
    """Mines bitcoin."""
    
    for i in range(100):
        print(f"{Fore.WHITE}Mining... {Fore.BLUE}{i}%")
        sleep(0.25)
    sleep(0.5)
    print(f"{Fore.WHITE}Mining... {Fore.BLUE}100%")

    if exists("./.btcmine"):
        with open("./.btcmine", "r") as btc_mine:
            total_amnt = float(btc_mine.read())
        total_amnt += amnt
        with open("./.btcmine", "w") as btc_mine:
            btc_mine.write(f"{total_amnt}")
    else:
        with open("./.btcmine", "w") as btc_mine:
            btc_mine.write(f"{amnt}")
            
    print(f"{Fore.GREEN}Added {amnt} BTC to your wallet")

def hunt(auto=False):
    """Mines bitcoin."""

    hunt_running = True
    connected = False

    for i in range(3): # retrying 3 times if no connection to the google.com
        print(f"{Fore.BLUE}Connecting to server...")
        sleep(3)

        # check for internet
        try:
            request = get("https://google.com", timeout=10) # check if internet is available
        except:
            print(f"{Fore.RED}Couldn't connect to server. Retrying.") # tries connecting to google.com again
            sleep(0.25)
        else:
            print(f"{Fore.GREEN}Connected to server!")
            connected = True
            break

    if connected == False:
        print(f"{Fore.RED}Couldn't connect to server. Check your internet connection.")

    # finding addresses
    while hunt_running:
        sleep(randint(500, 1700) / 1000) # sleeps for a random time between 500ms and 1700ms
        print(f"{Fore.WHITE}0x{token_hex(20)}", end=" ") # generate random address

        if randint(0, 100) <= 1: # 1/50 chance
            amnt = randint(1, 100) / 100
            if len(str(amnt)) == 3: # 0.7 BTC to 0.70 BTC
                print(f"{Fore.GREEN}[{amnt}0 BTC] (${round(amnt * 40000, 2)} USD)")
            else:
                print(f"{Fore.GREEN}[{amnt} BTC] (${round(amnt * 40000, 2)} USD)")
            
            if auto == False:    
                choice = None
                while choice not in ["y", "n"]:
                    choice = input(f"{Fore.YELLOW}Do you want to continue? (y/n) {Fore.WHITE}").lower()
                if choice == "n":
                    hunt_running = False
                else:
                    mine(amnt)
                    hunt_running = False
            else:
                mine(amnt)

        else:
            print(f"{Fore.RED}[0.00 BTC] ($0.00 USD)")

def balance():
    """Displays your balance."""

    if exists("./.btcmine"):
        with open("./.btcmine", "r") as btc_mine:
            amnt = float(btc_mine.read())
            print(f"{Fore.MAGENTA}Your balance is {amnt} BTC (${round(amnt * 40000, 2)} USD)")
    else:
        print(f"{Fore.MAGENTA}Your balance is 0.00 BTC ($0.00 USD)")

running = True

print(f"{Fore.WHITE}Welcome to {Fore.GREEN}Completely Legit and Real Bitcoin Miner v1.0!")
print(f"{Fore.YELLOW}(C) Scam Co. 1984-2022. All rights reserved.")
print(f"{Fore.WHITE}Type help and about for more informations.\n")

while running:
    command = input(f"{Fore.WHITE}> {Fore.GREEN}").lower()
    if command in ["balance", "bal"]:
        balance()

    elif command in ["hunt", "mine"]:
        hunt()
        
    elif command in ["hunt auto", "mine auto"]:
        hunt(True)

    elif command in ["exit", "quit", "close"]:
        print(f"{Fore.WHITE}Thank you for using {Fore.GREEN}Completely Legit and Real Bitcoin Miner v1.0!")
        running = False

    elif command.startswith("help"):
        if command == "help":
            print(f"{Fore.BLUE}Command list:")
            print(f"{Fore.GREEN}HELP: {Fore.WHITE}Sends this message.")
            print(f"{Fore.GREEN}MINE: {Fore.WHITE}Mines bitcoin.")
            print(f"{Fore.GREEN}MINE AUTO: {Fore.WHITE}Mines bitcoin (doesn't ask do you want to continue).")
            print(f"{Fore.GREEN}BALANCE: {Fore.WHITE}Displays your balance.")
            print(f"{Fore.GREEN}EXIT: {Fore.WHITE}Exits the program.")
            print(f"{Fore.GREEN}ABOUT: {Fore.WHITE}Displays information about the program.")
        else:
            command_to_help = command.split(" ")[1]

            if command_to_help in ["balance", "bal"]:
                print(f"{Fore.GREEN}BALANCE: {Fore.WHITE}Displays your balance.")
            elif command_to_help in ["hunt", "mine"]:
                print(f"{Fore.GREEN}MINE: {Fore.WHITE}Mines bitcoin.")
            elif command_to_help == "help":
                print(f"{Fore.GREEN}HELP: {Fore.WHITE}Displays this message.")
            elif command_to_help == "about":
                print(f"{Fore.GREEN}ABOUT: {Fore.WHITE}Displays information about the program.")
            elif command_to_help in ["exit", "quit", "close"]:
                print(f"{Fore.GREEN}EXIT: {Fore.WHITE}Exits the program.\n")
            print("If you want more info about a specific command, type help command.")

    elif command == "about":
        print(f"{Fore.BLUE}About Completely Legit and Real Bitcoin Miner v1.0:")
        print(f"{Fore.WHITE}This project was made because of some TikTok guy (@clxpedcode) that\nmade a fake Bitcoin mining program as a joke. I made \na better and more realistic one with more features.\n")
        print(f"{Fore.WHITE}Coded by: {Fore.GREEN}Viraxor")
        print(f"{Fore.WHITE}Original idea by: {Fore.GREEN}@clxpedcode")
        
    else:
        print(f"{Fore.RED}Invalid command!")
