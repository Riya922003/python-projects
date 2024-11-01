import random

# List of words to choose from
words = ["python", "hangman", "computer", "programming", "challenge"]

def choose_word():
    """Choose a random word from the list."""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Display the current state of the word."""
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def play_hangman():
    """Play the Hangman game."""
    while True:
        word_to_guess = choose_word()
        guessed_letters = []
        attempts = 6

        print("Welcome to Hangman!")

        while attempts > 0:
            print("\nWord: " + display_word(word_to_guess, guessed_letters))
            print("Attempts left:", attempts)
            print("Guessed letters:", " ".join(guessed_letters))

            guess = input("Guess a letter: ").lower()

            if len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("You've already guessed that letter.")
                elif guess in word_to_guess:
                    print("Good guess!")
                    guessed_letters.append(guess)
                    if set(word_to_guess).issubset(set(guessed_letters)):
                        print("Congratulations! You've guessed the word:", word_to_guess)
                        break
                else:
                    print("Wrong guess!")
                    guessed_letters.append(guess)
                    attempts -= 1
            else:
                print("Invalid input. Please enter a single letter.")

        if attempts == 0:
            print("You ran out of attempts. The word was:", word_to_guess)

        # Ask the player if they want to play again
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break

# Start the game
play_hangman()
