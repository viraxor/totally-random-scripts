import random
alphabet = list("AEPOZXLUGKISTVYN")
alphabet_zero = list("APZLGITY")

with open("gamegenie.gen", "w") as f:
    string = ""
    for i in range(2):
        string += random.choice(alphabet)
    string += random.choice(alphabet_zero)    
    for i in range(3):
        string += random.choice(alphabet) 
    
    f.write(string)
