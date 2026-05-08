print("          Welcome to Guessing Game        ")
print("          Here you have 4 attempts\nif you get the Jackpot number you'll be win the game")
print("Let's Start")

import numpy as np
rng=np.random.default_rng()

secrete_number=rng.integers(1,100)
guess= int(input("Guess the number: "))
count=1;

while guess != secrete_number:
    if guess < secrete_number:
        print("guess higher")
    else:
        print("Guess lower")
    count=count+1
    guess=int(input("Guess the number: "))

print("You won the game")

print("you used",count,"attempts to guess the correct number")