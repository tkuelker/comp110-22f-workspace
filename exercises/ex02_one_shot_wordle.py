"""EX02 - One-Shot Wordle game."""

i = 0
i_incorrect_placement = 0
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
secret_word: str = "python"
length_secret_word: int = len(secret_word)
guess: str = input(f"What is your {length_secret_word}-letter guess? ")
length_guess: int = len(guess)
guess_emojis: str = ""
possible_incorrect_placement: bool = False
character_not_found: bool = False
# setting up and assigning variable and indecies that are used later on in the program.
# Asks the user to enter a guess that has the same length as the secret word.

while length_secret_word != length_guess:
    guess = input(f"That was not {length_secret_word} letters! Try again: ")
    length_guess = len(guess)
# loops the program until the user enters a guess that is the same length as the secret word

while i < length_secret_word:
    if secret_word[i] == guess[i]:
        guess_emojis = guess_emojis + GREEN_BOX
# checks to see if the index of the guess is equal to the index of the secret word. If this is true a green box emoji is concatenated into the guess_emoji string.
    if secret_word[i] != guess[i]:
        possible_incorrect_placement = True
        while possible_incorrect_placement and i_incorrect_placement < length_secret_word:
            if secret_word[i_incorrect_placement] != guess[i]:
                i_incorrect_placement = i_incorrect_placement + 1
                character_not_found = True
            else:
                guess_emojis = guess_emojis + YELLOW_BOX
                possible_incorrect_placement = False
                character_not_found = False
# checks to see if the index of the guess can be found anywhere else in the secret word. If so, a yellow box emoji is concatenated into the guess_emoji string.
    if character_not_found and secret_word[i] != guess[i]:
        guess_emojis = guess_emojis + WHITE_BOX
# check to see if the index of the guess can not be found anywhere in the secret word. If this is the case a white box emoji is concatenated into the guess_emoji string.
    character_not_found = False
    incorrect_placement = False
    i_incorrect_placement = 0
    i = i + 1
# reassigns the variable used in the while statement to their original value and increase the index, i, by 1.

print(guess_emojis)
if secret_word == guess:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")
# the emojis that correspond to the user's guess are printed followed by a statement says if their guess was correct or not.


__author__ = "730609760"
