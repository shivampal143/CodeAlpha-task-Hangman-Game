# CodeAlpha-task-Hangman-Game

Create a simple text-based Hangman game where the player guesses a word one letter at a time. Simplified Scope: ● Use a small list of 5 predefined words (no need to use a file or API). ● Limit incorrect guesses to 6. ● Basic console input/output — no graphics or audio. Key Concepts Used: random, while loop, if-else, strings, lists.  give the project solution in simple and short

Here is a simple, short Python solution for the Hangman game that hits all your requirements.

Python
import random

# 1. Setup the game data
words = ["python", "coding", "player", "shadow", "matrix"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")

# 2. Main game loop
while attempts_left > 0:
    # Display the current word progress
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    
    print("\nWord: " + display_word.strip())
    print(f"Attempts left: {attempts_left}")
    
    # Check if the player has won
    if "_" not in display_word:
        print("Congratulations! You won!")
        break
        
    # Get player input
    guess = input("Guess a letter: ").lower()
    
    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single valid letter.")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue
        
    # Process the guess
    guessed_letters.append(guess)
    
    if guess in secret_word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        attempts_left -= 1

# 3. Game over condition
if attempts_left == 0:
    print(f"\nGame Over! The word was: {secret_word}")
How It Works:
random.choice(): Randomly picks one of your 5 predefined words.

while attempts_left > 0: Keeps the game running until the player runs out of guesses or breaks out early by winning.

for letter in secret_word: Loops through the secret word to print correctly guessed letters or underscores (_).

Input Validation: Ensures the player only types a single alphabetical letter and checks if they've already guessed it.

give the hangman game simple description for uploading in github

Here is a clean, simple, and professional description you can copy and paste directly into your GitHub repository's README.md file.

Simple Console Hangman Game
A minimalist, text-based Hangman game built in Python. This project is a beginner-friendly demonstration of core programming concepts, requiring no external libraries or complex setups.

Features
Random Word Selection: Picks a word at random from a predefined list of 5 words.

Turn-Based Gameplay: Players have exactly 6 incorrect guesses to uncover the hidden word.

Input Validation: Prevents players from wasting turns on invalid characters (numbers/symbols) or letters they've already guessed.

Pure Console Experience: Lightweight and runs entirely in the terminal without any graphics or audio.

Key Concepts Demonstrated
Loops (while and for)

Conditional logic (if-elif-else)

Data structures (lists and strings)

Randomization (random module)

User input handling and string manipulation

How to Run
Ensure you have Python installed on your machine.

Clone the repository or download the script file.

Open your terminal/command prompt and run:
