"""Ex03 - Structured Wordle game."""


from mimetypes import guess_all_extensions


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def contains_char (secret_word: str, guess_character: str) -> bool:
    """Checks if a str of length 1 is found in a str of any length."""
    assert len(guess_character) == 1
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == guess_character:
            return True
        i += 1
    return False


def emojified (guess_word: str, secret_word: str) -> str:
    """Checks if the characters in a guess word are in a secret word and returns color coded emojis."""
    assert len(guess_word) == len(secret_word)
    i: int = 0
    emojis: str = ""
    while i < len(secret_word):
        if secret_word[i] == guess_word[i]:
            emojis += GREEN_BOX
        elif contains_char(secret_word, guess_word[i]):
            emojis += YELLOW_BOX
        else:
            emojis += WHITE_BOX
        i += 1
    return emojis


def input_guess (expected_length: int) -> str:
    """Prompts the user for a guess of an expected length."""
    guess_word = input(f"Enter a {expected_length} character word: ")
    while len(guess_word) != expected_length:
        guess_word = input(f"That was not {expected_length} chars! Try again: ")
    return guess_word


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    number_of_guesses: int = 1
    guess_word: str = ""
    correct_guess: bool = True
    while number_of_guesses < 6 and correct_guess:
        print(f"=== Turn {number_of_guesses}/6 ===")
        print(emojified(input_guess(len(secret_word)), secret_word))
        if secret_word == guess_word:
            correct_guess = False
        else:
            number_of_guesses += 1
    if not correct_guess:
        print(f"You won in {number_of_guesses}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()


__author__ = "730609760"
