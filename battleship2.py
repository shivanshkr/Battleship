from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print (" ".join(row))

print ("Let's play Battleship!")
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

a = input("Player 1 enter your name:")
b = input("Player 2 enter your name:")

ship_rowA = random_row(board)
ship_colA = random_col(board)
#print (ship_rowA)
#print (ship_colA)

ship_rowB = random_row(board)
ship_colB = random_col(board)
#print (ship_rowB)
#print (ship_colB)

for turn in range(40):
    print ("Its  %s's turns"%a)
    guess_rowA = int(input("Guess Row(between 0 and 4):"))
    guess_colA = int(input("Guess Col(between 0 and 4):"))

    if guess_rowA == ship_rowB and guess_colA == ship_colB:
        print ("Congratulations! %s sunk %s battleship!\n%s WINS!!!!!"%(a,b,a))
        break
    else:
        if (guess_rowA < 0 or guess_rowA > 4) or (guess_colA < 0 or guess_colA > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_rowA][guess_colA] == "X"):
            print ("You guessed that one already.")
        elif(board[guess_rowA][guess_colA] == "Y"):
            print ("You missed %s battleship!"%b)
            board[guess_rowA][guess_colA] = "Z"
        elif(board[guess_rowA][guess_colA] == "Z"):
            print ("You guessed that one already.")
        else:
            print ("You missed %s battleship!"%b)
            board[guess_rowA][guess_colA] = "X"

    print_board(board)

    print ("Its %s's turns"%b)
    guess_rowB = int(input("Guess Row:"))
    guess_colB = int(input("Guess Col:"))

    if guess_rowB == ship_rowA and guess_colB == ship_colA:
        print ("Congratulations! %s sunk %s battleship!\n%s WINS!!!!!"%(b,a,b))
        break
    else:
        if (guess_rowB < 0 or guess_rowB > 4) or (guess_colB < 0 or guess_colB > 4):
            print ("Oops, that's not even in the ocean.")
        elif(board[guess_rowB][guess_colB] == "Y"):
            print ("You guessed that one already.")
        elif(board[guess_rowB][guess_colB] == "X"):
            print ("You missed %s battleship!"%a)
            board[guess_rowB][guess_colB] = "Z"
        elif(board[guess_rowB][guess_colB] == "Z"):
            print ("You guessed that one already.")
        else:
            print ("You missed %s battleship!"%a)
            board[guess_rowB][guess_colB] = "Y"
        if (turn == 40):
            print ("Game Over")
    print ("Turn", (turn + 1))
    print_board(board)
