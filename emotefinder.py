import requests
import random
import colorama

running = True

while running:
    link = f"https://cdn.discordapp.com/emojis/{random.randint(100000000000000000, 999999999999999999)}.png"
    response = requests.get(link)
    if response.status_code == 404:
        print(f"{colorama.Fore.RED}Invalid link:{colorama.Fore.WHITE} {link}")
    else:
        print(f"{colorama.Fore.GREEN}Valid code!{colorama.Fore.WHITE} {link}")
        running = False
