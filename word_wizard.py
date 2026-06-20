"""
WORD WIZARD
A simple letter-guessing game (Hangman-style).
Key Concepts Used: random, while loop, if-else, strings, lists
"""

import random


def get_random_word(word_list):
    """Pick a random word from the list."""
    return random.choice(word_list)


def display_hangman(wrong_guesses):
    """Return ASCII art matching the current number of wrong guesses."""
    stages = [
        """
           ------
           |    |
           |
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |    |
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   /
           |
        --------
        """,
        """
           ------
           |    |
           |    O
           |   /|\\
           |   / \\
           |
        --------
        """
    ]
    return stages[wrong_guesses]


def play_hangman():
    # A small predefined list of 5 words (no file or API needed)
    words = ["python", "hangman", "computer", "programming", "developer"]
    word = get_random_word(words)

    guessed_letters = []
    wrong_guesses = 0
    max_wrong_guesses = 6

    print("=" * 40)
    print("WELCOME TO WORD WIZARD")
    print("=" * 40)
    print(f"The word has {len(word)} letters.")
    print(f"You may make {max_wrong_guesses} incorrect guesses.\n")

    while wrong_guesses < max_wrong_guesses:
        # Build the current display string, e.g. "_ y t _ o n"
        display_word = ""
        for letter in word:
            if letter in guessed_letters:
                display_word += letter + " "
            else:
                display_word += "_ "

        print(display_hangman(wrong_guesses))
        print("Word: " + display_word)
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")
        if guessed_letters:
            print("Guessed so far: " + ", ".join(guessed_letters))

        # Win condition: no underscores left
        if "_" not in display_word:
            print("\nCongratulations! You guessed the word: " + word)
            break

        guess = input("\nGuess a letter: ").lower().strip()

        # Basic input validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter (a-z).\n")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.\n")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.\n")
        else:
            wrong_guesses += 1
            print(f"Sorry, '{guess}' is not in the word.\n")

    else:
        # This runs only if the while loop ended because guesses ran out
        print(display_hangman(wrong_guesses))
        print(f"\nGame over! You ran out of guesses. The word was: {word}")


def main():
    play_again = "yes"
    while play_again == "yes":
        play_hangman()
        play_again = input("\nPlay again? (yes/no): ").lower().strip()

    print("\nThanks for playing Word Wizard! Goodbye.")


if __name__ == "__main__":
    main()
