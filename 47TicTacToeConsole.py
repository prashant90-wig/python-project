def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i+1]} | {board[i+2]} ")
        if i< 6:
            print("-" * 12)
    print("\n")

def check_winner(board, player):

    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],    #rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],    #columns
        [0, 4, 8], [2, 4, 6]                #diagonals
    ]

    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False

def main():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 'X'
    
    print("Tic-Tac-Toe! Enter 0-8 for position")
    print_board(board)
    
    # Play 9 turns max
    for turn in range(9):
        # Get player move
        while True:
            try:
                pos = int(input(f"Player {player}, pick position (0-8): "))
                
                if pos < 0 or pos > 8:
                    print("Must be 0-8!")
                    continue
                
                if board[pos] != ' ':
                    print("Already taken!")
                    continue
                
                break
            except:
                print("Enter a number!")
        
        # Place mark
        board[pos] = player
        print_board(board)
        
        # Check if won
        if check_winner(board, player):
            print(f"Player {player} wins!")
            break
        
        # Switch player
        if player == 'X':
            player = 'O'
        else:
            player = 'X'
    else:
        print("It's a tie!")

if __name__ == "__main__":
    main()