
def createBoard(boardSize):
    board = []
    for row in range(boardSize): 
        board.append([]) 
        for col in range(boardSize):
            board[row].append(row * boardSize + col)
    return board
            
def printBoard(board):
    outputString = "" #empty string
    for row in board: 
        

        for col in row:
            outputString += f"[{col:2}]"
        outputString += "\n"
    print(outputString, end ="")

def getUserDir():
    
    validCommands = ['n','e','w','s']

    while True:
        userInput = input("Enter a direction (n,e,w,s): ")
        userInput = userInput.lower().strip()
        if userInput not in validCommands: 
            print("Not a valid command")
            continue 
        return userInput

b = createBoard(4)
printBoard(b)
u = getUserDir()