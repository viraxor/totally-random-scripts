import random
alphabet = list("abcdefghijklmnopqrstuvwxyz")

while True:
    string = ""
    for i in range(random.randint(5, 100)):
        string += random.choice(alphabet)
    print(string)
    
    n = input("Press ENTER to continue")