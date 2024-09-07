import random

thresh = 10
for i in range(300):
    thresh *= 10
number = random.randint(1, thresh)

guess = thresh // 2
guess_num = 1

increase = thresh // (2**guess_num)

all_guesses = []

while guess != number:
    while increase != 0:
        if number < guess: # you should go lower
            guess = guess - increase
        else: # you should go higher
            guess = guess + increase
        guess_num += 1
        increase = thresh // (2**guess_num)
        
        all_guesses.append(guess)
        
        if guess == number:
            print("The number was", guess)
            print("It took me", guess_num, "guesses")
            input()
            quit()
    
    increase = 1
    if number < guess: # you should go lower
        guess = guess - increase
    else: # you should go higher
        guess = guess + increase
    guess_num += 1
    
    all_guesses.append(guess)
    
    if guess_num > 1000:
        print("I couldn't find the number", number)
        print("Last guess", guess)
        
        s = ""
        with open("guesses.txt", "w") as f:
            for guess in all_guesses:
                s += f"{guess}\n"
            f.write(s)
        input()
        quit()

if guess == number:    
    print("The number was", guess)
    print("It took me", guess_num, "guesses")
input()