import random

def guess_the_number():
    # 1. Generate a random secret number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("🔢 Welcome to the Guess the Number Game! 🔢")
    print("I am thinking of a number between 1 and 100.")
    print("Can you figure out what it is?")
    
    # 2. Main game loop
    while True:
        try:
            # Get the player's guess
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            # 3. Check the guess against the secret number
            if guess < secret_number:
                print("📉 Too low! Try a higher number.")
            elif guess > secret_number:
                print("📈 Too high! Try a lower number.")
            else:
                print(f"🎉 Congratulations! You guessed the number in {attempts} attempts!")
                break # Exit the game loop when they win
                
        except ValueError:
            # Prevents the game from crashing if someone types a letter or symbol
            print("❌ Invalid input. Please enter a valid whole number.")

if __name__ == "__main__":
    guess_the_number()
