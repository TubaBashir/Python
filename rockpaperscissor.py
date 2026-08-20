import random

def play_game():
    # 1. Setup options and scores
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0
    
    print("✊ ✋ ✌️ Welcome to Rock, Paper, Scissors! ✌️ ✋ ✊")
    print("Type 'quit' at any time to exit the game.\n")
    
    while True:
        # 2. Get and clean user input
        user_choice = input("Choose rock, paper, or scissors: ").strip().lower()
        
        if user_choice == 'quit':
            print("\nThanks for playing!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break
            
        if user_choice not in options:
            print("Invalid choice. Please type rock, paper, or scissors.\n")
            continue
            
        # 3. Computer makes a random choice
        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")
        
        # 4. Determine the winner
        if user_choice == computer_choice:
            print("It's a tie!\n")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("🎉 You win this round!\n")
            user_score += 1
        else:
            print("😢 Computer wins this round!\n")
            computer_score += 1
            
        # 5. Display current score
        print(f"Scoreboard -> You: {user_score} | Computer: {computer_score}")
        print("-" * 30)

# Run the game
if __name__ == "__main__":
    play_game()
