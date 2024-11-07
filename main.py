
boardSize = 4
board = []
for row in range(boardSize): 
    board.append([]) 
    for col in range(boardSize):
        board[row].append(row * boardSize + col)
        

print(board) 