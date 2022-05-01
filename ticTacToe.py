# First line here making sure my Github is set up properly

def main():
    print("Hello World")
    drawGameBoard()

def drawGameBoard():
    squareOne = "1"
    squareTwo = "2"
    squareThree = "3"
    squareFour = "4"
    squareFive = "5"
    squareSix = "6"
    squareSeven = "7"
    squareEight = "8"
    squareNine = "9"
    print("|--|--|--|")
    print("| "+squareOne+"| "+squareTwo+"| "+squareThree+"|")
    print("|--+--+--|")
    print("| "+squareFour+"| "+squareFive+"| "+squareSix+"|")
    print("|--+--+--|")
    print("| "+squareSeven+"| "+squareEight+"| "+squareNine+"|")
    print("|--|--|--|")
    

if __name__ == "__main__":
    main()

