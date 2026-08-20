def print_board(board):
    """Prints the current state of the game board."""
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

def check_win(board, player):
    """Checks if the current player has won the game."""
    # All 8 possible winning combinations (rows, columns, diagonals)
    win_conditions = [, [3, 4, 5], [6, 7, 8], # Horizontal rows, [1, 4, 7], [2, 5, 8], # Vertical columns, [2, 4, 6]             # Diagonals
    ]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def tic_tac_toe():
    # Initialize the board with numbers 1-9 to show positions
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    moves_played = 0

    print("❌ Tic-Tac-Toe Game ⭕")
    print("Players take turns choosing positions (1-9) as shown below:")
    
    while moves_played < 9:
        print_board(board)
        
        # 1. Get validated user input
        try:
            choice = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
        except ValueError:
            print("❌ Invalid input! Please enter a whole number between 1 and 9.")
            continue
            
        # 2. Check if the chosen index is valid and not already taken
        if choice < 0 or choice > 8:
            print("❌ Position out of bounds! Choose a number between 1 and 9.")
            continue
        if board[choice] == "X" or board[choice] == "O":
            print("❌ Position already taken! Try another square.")
            continue
            
        # 3. Make the move
        board[choice] = current_player
        moves_played += 1
        
        # 4. Check for a winner
        if check_win(board, current_player):
            print_board(board)
            print(f"🎉 Congratulations! Player {current_player} wins the game!")
            return
            
        # 5. Alternate players (Switch between X and O)
        current_player = "O" if current_player == "X" else "X"

    # 6. If the loop finished without a return, it's a tie
    print_board(board)
    print("🤝 It's a tie game! Well played both.")

if __name__ == "__main__":
    tic_tac_toe()
