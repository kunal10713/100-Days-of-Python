import random

# Define constants for the game
EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def get_attempts_based_on_difficulty(level):
    """
    Returns the number of attempts based on the chosen difficulty level.
    """
    if level == 'easy':
        return EASY_ATTEMPTS
    elif level == 'hard':   
        return HARD_ATTEMPTS
    else:
        print("Invalid difficulty level. Defaulting to 'easy'.")
        return EASY_ATTEMPTS

def guess_number(final_number):
    """
    Prompts the user to guess the number and provides feedback.
    Returns 1 if the guess is incorrect, 0 if correct.
    """
    try:
        guessed_number = int(input("Make a guess: "))
    except ValueError:
        print("Please enter a valid number.")
        return 1

    if guessed_number > final_number:
        print("Too high.\nGuess again.")
        return 1
    elif guessed_number < final_number:
        print("Too low.\nGuess again.")
        return 1
    else:
        print(f"You got it! The answer was {final_number}.")
        return 0

def number_guessing_game():
    """
    Main function to run the number guessing game.
    """
    final_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    num_attempts = get_attempts_based_on_difficulty(level)
    
    for attempt in range(num_attempts, 0, -1):
        print(f"You have {attempt} attempts remaining to guess the number.")
        
        guess_status = guess_number(final_number)
        
        if guess_status == 0:
            break
        
        if attempt == 1 and guess_status == 1:
            print(f"You've run out of guesses. The number was {final_number}.")

# Run the game
number_guessing_game()
