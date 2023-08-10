import random
alphabet = list("AEPOZXLUGKISTVYN")

char_num = 6

with open("gamegenie.gen", "w") as f:
    string = ""
    for i in range(char_num):
        string += random.choice(alphabet)
    
    f.write(string)