# Clancy Thomas 
# CSE 210-01
# Tic-Tac-Toe Game

def main():
    squareList = ['1','2','3','4','5','6','7','8','9']
    turns = 0
    winner = "none"
    while (turns<9):
        winner = checkForWinner(squareList)
        if winner=="none":
            drawGameBoard(squareList)
            if ((turns+1)%2 == 1):
                squareList = playerChoice('x', squareList)
            else:
                squareList = playerChoice('o', squareList)
            turns += 1
        else:
            drawGameBoard(squareList)
            print("Player "+winner+" wins!! Good game!")
            turns = 100
    if (turns==9):
        drawGameBoard(squareList)
        print("No winner! It ends in a draw! Better luck next time!!!")
    print("Thank you for playing!")



def drawGameBoard(squareList):
    print("\n|--|--|--|")
    print("| "+squareList[0]+"| "+squareList[1]+"| "+squareList[2]+"|")
    print("|--+--+--|")
    print("| "+squareList[3]+"| "+squareList[4]+"| "+squareList[5]+"|")
    print("|--+--+--|")
    print("| "+squareList[6]+"| "+squareList[7]+"| "+squareList[8]+"|")
    print("|--|--|--|\n")

def playerChoice(player, squareList):
    output = "NOPE"
    openSquare = True
    if player.lower() == "x":
        output = 'X'
    elif player.lower() == "o":
        output = 'O'
    else:
        output = "ERROR"
    while (openSquare):    
        playerChoice = int(input("Player "+output+"! Where do you want to put your "+output+"? Type a number (1-9) and then hit enter: "))
        if (squareList[playerChoice-1] != "X" and squareList[playerChoice-1] != "O"):
            squareList[playerChoice-1] = output
            openSquare = False
        else:
            print("\nThat square has been chosen already! Try again!\n")

    return squareList

def checkForWinner(squareList):
    if (squareList[0] == squareList[1] and squareList[1] == squareList[2]): 
        winner = squareList[0]
    elif (squareList[0] == squareList[3] and squareList[3] == squareList[6]):
        winner = squareList[0]
    elif (squareList[0] == squareList[4] and squareList[4] == squareList[8]):
        winner = squareList[0]
    elif (squareList[1] == squareList[4] and squareList[4] == squareList[7]):
        winner = squareList[1]
    elif (squareList[2] == squareList[5] and squareList[5] == squareList[8]):
        winner = squareList[2]
    elif (squareList[2] == squareList[4] and squareList[4] == squareList[6]):
        winner = squareList[2]
    elif (squareList[3] == squareList[4] and squareList[4] == squareList[5]):
        winner = squareList[3]
    elif (squareList[6] == squareList[7] and squareList[7] == squareList[8]):
        winner = squareList[6]
    else:
        winner = "none"
    
    return winner

if __name__ == "__main__":
    main()

