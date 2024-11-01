# Initialize the game board
board = [" "] * 9

def print_board():
    print("-------------")
    print("|", board[0], "|", board[1], "|", board[2], "|")
    print("-------------")
    print("|", board[3], "|", board[4], "|", board[5], "|")
    print("-------------")
    print("|", board[6], "|", board[7], "|", board[8], "|")
    print("-------------")

def check_winner(player):
    # Check rows, columns, and diagonals for a win
    for i in range(3):
        if board[i * 3] == board[i * 3 + 1] == board[i * 3 + 2] == player:
            return True
        if board[i] == board[i + 3] == board[i + 6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def start_game():
    print("Welcome to Tic Tac Toe!")
    print_board()
    player = "X"

    while True:
        try:
            n = int(input(f"Player {player}, make your move (1-9): ")) - 1
            if n < 0 or n >= 9:
                print("Invalid input, please enter a number between 1 and 9.")
                continue
            if board[n] == " ":
                board[n] = player
            else:
                print("Invalid move, that space is already taken! Try again.")
                continue
            
            print_board()  # Print the board after the move
            
            if check_winner(player):
                print(f"Congratulations Player {player}, you won the game!")
                break
            
            if " " not in board:
                print("It's a tie!")
                break
            
            # Switch players
            player = "O" if player == "X" else "X"

        except ValueError:
            print("Invalid input, please enter a number.")

# Start the game
start_game()
