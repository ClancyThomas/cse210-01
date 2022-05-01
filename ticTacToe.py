# First line here making sure my Github is set up properly

def main():
    squareList = ['1','2','3','4','5','6','7','8','9']
    turns = 0
    while (turns<9):
        drawGameBoard(squareList)
        if ((turns+1)%2 == 1):
            squareList = playerChoice('x', squareList)
        else:
            squareList = playerChoice('o', squareList)
        turns += 1

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
    if player.lower() == "x":
        output = 'X'
    elif player.lower() == "o":
        output = 'O'
    else:
        output = "ERROR"
    playerChoice = int(input("Player "+output+"! Where do you want to put your "+output+"? Type a number (1-9) and then hit enter: "))
    squareList[playerChoice-1] = output
    return squareList


if __name__ == "__main__":
    main()

