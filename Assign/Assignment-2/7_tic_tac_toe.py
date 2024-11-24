def print_board(board):
    """
    Print the Tic-Tac-Toe board.
    """
    print("\n".join([" | ".join(row) for row in board]))
    print()

def check_winner(board, player):
    """
    Check if the given player has won.
    
    :param board: The Tic-Tac-Toe board (list of lists)
    :param player: The player symbol to check (str)
    :return: True if the player has won, otherwise False
    """
    # Check rows and columns
    for i in range(3):
        if all([cell == player for cell in board[i]]) or all([board[j][i] == player for j in range(3)]):
            return True
    
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True
    
    return False

def is_board_full(board):
    """
    Check if the board is full.
    
    :param board: The Tic-Tac-Toe board (list of lists)
    :return: True if the board is full, otherwise False
    """
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe():
    """
    Main function to run the Tic-Tac-Toe game.
    """
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        
        try:
            row = int(input(f"Player {current_player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {current_player}, enter the column (0, 1, or 2): "))
            
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2.")
                continue
            
            if board[row][col] != " ":
                print("Cell already taken. Choose another cell.")
                continue
            
            board[row][col] = current_player
            
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            
            if is_board_full(board):
                print_board(board)
                print("The game is a tie!")
                break
            
            current_player = "O" if current_player == "X" else "X"
        
        except ValueError:
            print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    tic_tac_toe()
