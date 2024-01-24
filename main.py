

# Print board
def printBoard(board):
    print("\n")
    print("   A B C")
    for y in range (3):
        print(y,end="| ")
        for x in range (3):
            print(board[y][x],end = "")
            if x != 2:
                print("|",end = "")
        print("\n | -----")
    return

def placeMove(board, player, x, y):
    '''
    Player: string
    x: int
    y: int
    '''
    if (0<=y<=2 or 0<=x<=2):
        print("error, value out of range")
        return

    board[x][y] = player
    return
    
def checkWin(board):
    for i in range 3:
        if( board[i][i] == board[i][i+1] == board[i][i+2] )

def main():
    # Define board
    board = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

    printBoard(board)
    placeMove(board,"X",2,0)
    printBoard(board)

    return




main()
