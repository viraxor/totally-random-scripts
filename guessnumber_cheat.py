thresh = int(input())

guess = round(thresh // 2)
print(guess)
guess_num = 1

increase = thresh // (2**guess_num)

r = "a"

while r != "e":
    while increase != 0:
        r = input()
        if r == "l":
            guess = round(guess - increase)
        elif r == "h":
            guess = round(guess + increase)
        guess_num += 1
        increase = thresh // (2**guess_num)
        print(guess)
       
    increase = 1
    r = input() 
    if r == "l":
        guess = round(guess - increase)
    elif r == "h":
        guess = round(guess + increase)