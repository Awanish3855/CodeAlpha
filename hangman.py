
import random

def play_hangman():
    words = ["python", "computer", "hangman", "keyboard", "program"]
    secret_word = random.choice(words)
    guessed_letters = set()
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        display = ""
        for letter in secret_word:
            if letter in guessed_letters:
                display += letter + " "
            else:
                display += "_ "
        print("\nWord: " + display)
        print("Attempts left:", attempts_left)

        if "_" not in display:
            print("You won! The word was:", secret_word)
            break

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess not in secret_word:
            attempts_left -= 1
            print("Wrong guess!")

    if attempts_left == 0:
        print("You lost! The word was:", secret_word)

play_hangman()