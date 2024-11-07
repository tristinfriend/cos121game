
def createBoard(boardSize):
    board = []
    for row in range(boardSize): 
        board.append([]) 
        for col in range(boardSize):
            board[row].append(row * boardSize + col)
    return board
            
def printBoard(board):
    for row in board: 


        for col in row:
            print(f"[{col:2}]", end="")
        print() 



b = createBoard(4)
printBoard(b)