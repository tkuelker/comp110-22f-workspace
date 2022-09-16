"""Ex03 - Structured Wordle game."""


def contains_char(secret_word: str, guess_character: str) -> bool:
    """Checks if a str of length 1 is found in a str of any length."""
    assert len(guess_character) == 1
    i: int = 0
# contains_char is a def function that needs two str as parameters and it returns a bool value. This function checks to see if a letter from the users guess can be found elsewhere in the secret word. The length of the guess_charater str must be 1 for this function to continue. 
    while i < len(secret_word):
        if secret_word[i] == guess_character:
            return True
        i += 1
    return False
# This while loop compares each indice in the sercet word to guess_character. If there is a match, True will be returned, and if not the index will increase by one and the loop will repeat. If no match is found False will be returned.


def emojified(guess_word: str, secret_word: str) -> str:
    """Checks if the characters in a guess word are in a secret word and returns color coded emojis."""
    assert len(guess_word) == len(secret_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i: int = 0
    emojis: str = ""
# emojified is a def function that needs two str as parameters and it returns a str. This function checks to see if the charaters of the guess_word are equal to the characters of the sercet word and assigns different colored emoji rectangles depending if the characters are a direct match, a match with a different index, or not a match. The length of guess_word must be equal to the length of secret_word for the function to continue.
    while i < len(secret_word):
        if secret_word[i] == guess_word[i]:
            emojis += GREEN_BOX
        elif contains_char(secret_word, guess_word[i]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis
# This while loop compares the indices of secret_word and guess_word. If the indices match a green box is concatinated with the str emojis. If the indices do not match, contains_char is called with parameters secret_word and the current index of guess_word. If contains_char returns True a yellow box is concatinated with emojis, and if not a white box is concatinated with emojis. Once i is equal to the length of secret_word, the str emojis is returned.


def input_guess(expected_length: int) -> str:
    """Prompts the user for a guess of an expected length."""
    guess_word = input(f"Enter a {expected_length} character word: ")
    length_guess_word: int = len(guess_word)
# input_guess is a def function that needs one int as a parameter and returns a str. This function prompts the user to enter their guess for the secret_word until the length of the users guess is equal to the length of secret_word.
    while length_guess_word != expected_length:
        guess_word = input(f"That wasn't {expected_length} chars! Try again: ")
        length_guess_word = len(guess_word)
    return guess_word
# This while loop runs while the length of guess_word is not equal to the length of secret_word. This loop keeps prompting the user to enter a guess that is equal to the length of secret_word. Once the users has entered an acceptable length guess_word, the loop ends and guess_word is returned.


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    number_of_guesses: int = 1
    correct_guess: bool = False
# main is a def function that brings together all of the previously defined functions to run the wordle game. Here is secret word is defined as "codes" and an int variable is defined that tracks the number of times the user has guessed, called number_of_guesses. Also, correct_guess is defined as a bool variable that is initialized to False to show that the user has not guessed correctly.
    while number_of_guesses <= 6 and not correct_guess:
        print(f"=== Turn {number_of_guesses}/6 ===")
        guess_word = input_guess(len(secret_word))
        print(emojified(guess_word, secret_word))
        if secret_word == guess_word:
            correct_guess = True
        else:
            number_of_guesses += 1
    if correct_guess:
        print(f"You won in {number_of_guesses}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")
# This while loop continues to loop as long as guess_word does not equal secret_word and number_of_guesses is less than or equal to 6. First the number of turns is printed out. Then the user is prompted to enter a guess that is equal in length to secret_word by calling the input_guess function. Using the returned guess_word and secret_word as parameters, emojified is called and returns as string of emojis that is printed. If the guess_word is equal to the secret_word, correct_guess is assigned True and the while loop ends. Then text is printed that says how many turns if took the user to win. However, if secret_word does not equal guess_word, the index of number_of_guesses increases by one and the while loop repeats. If the user runs out of turns before they guess the secret word, the loop ends that a statement is printed telling them that they ran out of turns and to play again.


if __name__ == "__main__":
    main()


__author__ = "730609760"
