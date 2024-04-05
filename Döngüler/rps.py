import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

uWon = "Congratulation, you won!\n"
uLost = "Unfortunately, you lost!\n"
well = "It is well!\n"

scissorsPaper = "Scissors beats Paper!"
paperRock = "Paper beats Rock!"
rockScissors = "Rock beats Scissors!"

acceptableValues = ("rock", "1", "a", "r",
       "paper", "2", "b", "p",
       "scissors", "3", "c", "s")

def getInput():

    print("1 || A || R ||", rock, "\n2 || B || P ||", paper, "\n3 || C || S ||", scissors)
    
    userInput = input("\nPlease make your choice!\n")

    userInput = userInput.strip().lower()

    return userInput

while True:

    chosenOnes = "\n"

    userChoice = getInput()

    if userChoice in acceptableValues:

        if (userChoice == acceptableValues[0] or userChoice == acceptableValues[1] or
                userChoice == acceptableValues[2] or userChoice == acceptableValues[3]):

            userChoice = 1
            chosenOnes += rock

        elif (userChoice == acceptableValues[4] or userChoice == acceptableValues[5] or
              userChoice == acceptableValues[6] or userChoice == acceptableValues[7]):

            userChoice = 2
            chosenOnes += paper

        else:

            userChoice = 3
            chosenOnes += scissors

        pcChoice = random.randint(1, 3)
        chosenOnes += " - "

        match pcChoice:
            case 1:

                chosenOnes += rock
                print(chosenOnes)

                match userChoice:
                    case 2:
                        print(paperRock)
                    case 3:
                        print(rockScissors)

            case 2:

                chosenOnes += paper
                print(chosenOnes)

                match userChoice:
                    case 1:
                        print(paperRock)
                    case 3:
                        print(scissorsPaper)

            case 3:

                chosenOnes += scissors
                print(chosenOnes)

                match userChoice:
                    case 1:
                        print(rockScissors)
                    case 2:
                        print(scissorsPaper)


        if userChoice == 1 and pcChoice == 3:
            print(uWon)
        elif userChoice == 2 and pcChoice == 1:
            print(uWon)
        elif userChoice == 3 and pcChoice == 2:
            print(uWon)
        elif userChoice == pcChoice:
            print(well)
        else:
            print(uLost)

    else:
        print("\n**** INCORRECT ENTRY ****\n")
