# Initialize the board
board = [["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["0", "0", "0", "0", "0"],
         ["A", "B", "C", "D", "E"]]

# Initialize the pointers to the first available position in each column
pointers = [4, 4, 4, 4, 4]

# Show the current state of the board
def showBoard():
    """This function prints the board on the screen"""
    global board
    for row in range(0, 6):
        for column in range(0, 5):
            print(board[row][column], "   ", end='')
        print()

# Update the board with the player's move
def updateBoard(colour, column):
    global board, pointers
    # Convert the column to column number
    colNumber = {"a": 0, "b": 1, "c": 2, "d": 3, "e": 4}
    if column not in colNumber:
        print("The column you have chosen is not valid.")
        updateBoard(colour, input("Please choose another column "))
    cNumber = colNumber[column]
    # Update the board by adding the player's colour to the top of the column
    if pointers[cNumber] != -1:
        board[pointers[cNumber]][cNumber] = colour
        pointers[cNumber] -= 1
    else:
        print("The column you have chosen is full.")
        updateBoard(colour, input("Please choose another column "))

# Check if there is a winner
def isWinner():
    global board

    # Check rows
    for row in range(6):
        for column in range(3):
            if all(board[row][column+i] == board[row][column] != "0" for i in range(4)):
                return True

    # Check columns
    for column in range(5):
        for row in range(3):
            if all(board[row+i][column] == board[row][column] != "0" for i in range(4)):
                return True

    return False

# Play the game
def play():
    showBoard()
    # Ask players for their names and store them in two variables
    player_1 = input("Enter first player name ")
    player_2 = input("Enter second player name ")
    # Inform players about their letter allocation: player 1 will have Y and player 2 will have R
    print(player_1 + " will use Yellow colour (Y), while " + player_2 + " will use red (R)")
    # Set winner to False
    winner = False
    attempt = 0
    while not winner: # While there is no winner
        # If attempt is odd, it's player 1's turn (Yellow), otherwise it's player 2's turn (Red)
        if attempt % 2 == 0:
            current_player = player_1
            colour = "Y"
        else:
            current_player = player_2
            colour = "R"
        # Ask the current player for the column they want to use (A, B, C, D, E)
        print()  # Just to improve the screen presentation
        print(current_player + " turn : ")
        column = input("Which column do you want to choose? (type A, B, C, D, or E)  ")
        updateBoard(colour, column.lower()) # Call the updateBoard function to update the board
        showBoard()  # Show the board to the players
        winner = isWinner() # Check if there is a winner
        attempt += 1
    print("The winner is " + current_player)

# Main program
play()