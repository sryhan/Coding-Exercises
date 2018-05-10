"""
Make a two-player Rock-Paper-Scissors game. (
Hint: Ask for player plays (using input), compare them, print out a message of
congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

-Rock beats scissors
-Scissors beats paper
-Paper beats rock
"""


def rockPaperSci():


    prompt1 = input("Rock, Paper, or Scissors? ")
    prompt2 = input("Rock, Paper, or Scissors? ")

    while prompt1 != "quit" or prompt2 == "quit":
        if (prompt1 == "Rock" or prompt2 == "Rock") and (prompt2 == "Scissors" or prompt1 == "Scissors"):
            print("Rock beats Scissors")
        elif (prompt1 == "Paper" or prompt2 == "Paper") and (prompt2 == "Rock" or prompt1 == "Rock"):
            print("Paper beats Rock")
        elif (prompt1 == "Scissors" or prompt2 == "Scissors") and (prompt1 == "Paper" or prompt2 == "Paper"):
            print("Scissors beats Paper")
        elif prompt1 == prompt2:
            print("Tie!")

rockPaperSci()
