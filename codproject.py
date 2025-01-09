import random

def select_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman():
    word_list = ["script", "programming", "python", "programer", "java"]
    word_to_guess = select_random_word(word_list)
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman! Guess the word one letter at a time.")

    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nWord: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")

        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter. Try another one.")
            continue

        guessed_letters.add(guess)

        if guess in word_to_guess:
            print("Good guess!")
            if all(letter in guessed_letters for letter in word_to_guess):
                print(f"\nCongratulations! You guessed the word: {word_to_guess}")
                break
        else:
            print("Wrong guess!")
            incorrect_guesses += 1

    if incorrect_guesses == max_incorrect_guesses:
        print(f"\nGame over! You've been hanged. The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
