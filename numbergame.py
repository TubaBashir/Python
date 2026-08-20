

import random

def number_guessing_game():
    # 1. Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    
    # 2. Start the game loop
    while True:
        try:
            # Get player's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # 3. Check the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break # Exit the game loop
                
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
