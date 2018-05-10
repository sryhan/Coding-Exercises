"""
Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
guess the number, then tell them whether they guessed too low, too high, or
exactly right.

Extras:

-Keep the game going until the user types “exit”
-Keep track of how many guesses the user has taken, and
-when the game ends, print this out.
"""

import random

randNum = random.randint(1,9)
count = 0

while True:
    count += 1
    guessNum = int(input("Guess the number (type quit to quit): "))
    if guessNum == 'quit':
        break
    elif guessNum == randNum:
        print("Correct, the number was " + str(randNum))
        break
    elif guessNum > randNum:
        print("Too high, guess again")
        continue
    elif guessNum < randNum:
        print("Too low, guess again")
        continue

print("It took " + str(count) + " tries")
