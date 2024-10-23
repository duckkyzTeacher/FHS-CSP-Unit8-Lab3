# Initialize the Tic-Tac-Toe board
board = []

def display_board(board):
    print()
    print("-" * 13)
    


def get_move(player):
    while True:
        row = 0 #get user input
        #Check row
        
        col = 0 #get user input
        #Check column
        
        
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

    #Check other cases

    return isWinner  




def play_game():
    current_player = "X" #other player is "O"
    for turn in range(9):
        display_board(board)
        row, col = get_move(current_player)
        make_move(board, row, col, current_player)
        winner = check_winner(board)
        if winner:
            display_board(board)
            print(f"Player {winner} wins!")
            return
        
        #Swap players here
        
            
    display_board(board)
    print("It's a tie!")

play_game()

