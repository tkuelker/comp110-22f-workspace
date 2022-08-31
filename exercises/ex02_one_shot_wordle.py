"""EX02 - One-Shot Wordle game"""

i = 0
i_incorrect_placement = 0
secret_word: str = "python"
length_secret_word: int = len(secret_word)
guess: str = input(f"What is your {length_secret_word}-letter guess? ")
length_guess: int = len(guess)
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
guess_emojis: str = ""
incorrect_placement: bool = False
character_not_found: bool = False


while length_secret_word != length_guess:
    guess = input(f"That was not {length_secret_word} letters! Try again: ")
    length_guess = len(guess)


while i < length_secret_word:
    if secret_word[i] == guess[i]:
        guess_emojis = guess_emojis + GREEN_BOX
    if secret_word[i] != guess[i]:
        incorrect_placement = True
        while i_incorrect_placement < length_secret_word and incorrect_placement == True:
            if secret_word[i_incorrect_placement] != guess[i]:
                i_incorrect_placement = i_incorrect_placement + 1
                character_not_found = True
            else:
                guess_emojis = guess_emojis + YELLOW_BOX
                incorrect_placement = False
                character_not_found = False
    if secret_word[i] != guess[i] and character_not_found == True:
        guess_emojis = guess_emojis + WHITE_BOX
    character_not_found = False
    incorrect_placement = False
    i_incorrect_placement = 0
    i = i + 1

print(guess_emojis)


if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")


__author__ = "730609760"
