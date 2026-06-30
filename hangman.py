import random

# 1. Setup the game data
words = ["python", "coding", "player", "shadow", "matrix"]
secret_word = random.choice(words)
guessed_letters = []
attempts_left = 6

print("Welcome to Hangman!")

# 2. Main game loop
while attempts_left > 0:
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