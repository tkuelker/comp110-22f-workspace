"""Example of conditional if-else statements"""

secret: int = 4

print("Guess how many fingers I have behind my back.")
guess: int = int(input("What is your guess? "))

if guess == secret:
    print("Correct!")
else:
    print("Wrong!")

print("Game over")