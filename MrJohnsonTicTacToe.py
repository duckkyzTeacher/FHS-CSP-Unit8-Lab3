# Initialize the Tic-Tac-Toe board
board = [[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

def display_board(board):
    print()
    print("-" * 13)
    for row in board:
        print("|", end=" ")
        for col in row:
            print(col, end = " | ")
        print()
        print("-" * 13)


def get_move(player):
    while True:
        row = int(input(f"Player {player}, enter your move (row 0-2): "))
        
        while row < 0 or row > 2:
            print("Im sorry that is an invlaid row")
            row = int(input(f"Player {player}, enter your move (row 0-2): "))
            
        col = int(input(f"Player {player}, enter your move (column 0-2): "))    
        while col < 0 or col > 2:
            print("Im sorry that is an invlaid col")
            col = int(input(f"Player {player}, enter your move (column 0-2): "))
            
        if board[row][col] == " ":
            return row, col
        else:
            print("That cell is already taken. Choose another.")

def make_move(board, row, col, player):
    board[row][col] = player


def check_winner(board):
    isWinner = None # No winner yet
    
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]  # Return the winner for this case

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return isWinner  




def play_game():
    current_player = "X"
    for turn in range(9):
        display_board(board)
        row, col = get_move(current_player)
        make_move(board, row, col, current_player)
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            return
        if current_player == "X":
            current_player = "O"
        elif current_player == "O":
            current_player = "X"
            
    display_board(board)
    print("It's a tie!")

play_game()

