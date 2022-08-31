"""EX02 - One-Shot Wordle game"""

i = 0

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

secret_word: str = "python"
length_secret_word: int = len(secret_word)
guess: str = input(f"What is your {length_secret_word}-letter guess? ")
length_guess: int = len(guess)
guess_emojis: str = ""

while length_secret_word != length_guess:
    guess = input(f"That was not {length_secret_word} letters! Try again: ")
    length_guess = len(guess)

while i < length_secret_word:
    if secret_word[i] == guess[i]:
        guess_emojis = guess_emojis + GREEN_BOX
    else:
        guess_emojis = guess_emojis + WHITE_BOX

print(guess_emojis)


if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")


__author__ = "730609760"
