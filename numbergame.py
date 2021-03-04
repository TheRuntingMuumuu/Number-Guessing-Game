"""
This is just a program that I made when I thought of an old number guessing game that I played once.
Made by TheRuntingMuumuu
Concept by Nundodo
"""
playagain = True #so that they will play the game the first time
while playagain == True:
    #Just defining some variables
    complete = False
    numberGuess = 0 #Defining base values
    numberOfTries = 0 #base value
    scoreMultiplyer = 1 #default value
    chosenNumbers = False #this is needed to tell the program that you have not chosen numbers yet
    lowerNumber = 1 #again just defines this so it does not error out later
    upperNumber = 100 #just defines this so it does not error out later

    import random #needed for the random number generator
    import os #needed to clear the screen
    def clearScreen(): #clears screen
        if os.name == 'nt': #is it windows
            os.system('cls') #windows clear
        else:
            os.system('clear') #macos/linux clear

    def fullLine(): #makes a full width line in the terminal
        width = os.get_terminal_size().columns #finds the size of the terminal
        print("-" * width)

    #----->This part shows the credits<-----
    clearScreen()
    fullLine()
    print("This is a Number Guessing Game\nCoded by TheRuntingMuumuu\nConcept by Nundodo")
    fullLine()
    print("\n")

    #----->This part shows the rules<-----
    rules = input("Welcome to the Number Guessing Game. Do you want to see the rules? --> ") #assignes rules variable to the input from the user
    try: #try this but if it errors out, it will go to except
        if rules.lower().strip()[0] == 'y' or rules.strip()[0] == "1": #it checks if the first letter of the var rules is y, or 1
            print("The rules of this game are this. \n\t Pick the lower and upper values of the range that the computer will pick the value in \n\t Guess the number, and it will tell you whether you arr too high, or too low. \n\t You want to guess the number in as little tries as possible. \n")
            input("Press ENTER to continue -->")
    except (IndexError, ValueError): #If they did not enter a y, or 1
        print("Defaulting to No")

    #----->This part takes the user input for the numbers and determines the number<-----
    while chosenNumbers == False:
        try: #it will try this, if the user does not do an integer, it will go to except
            lowerNumber = int(input("\n\nWhat is the lower value for the range --> "))
            upperNumber = int(input("What is the upper value for the range --> "))
            number = random.randint(lowerNumber, upperNumber) #picks the number
            chosenNumbers == True #only gets here if no errors, in which case the numbers were chosen
            break
        except (IndexError, ValueError): #if the user did not choose an integer
            if lowerNumber > upperNumber: #chooses the error code, this one is if the lower is bigger than upper
                print("\nThe lower number is higher than the upper number.")
                print("Please make sure that the first number has a higher numerical value than the second one.")
                print("\n\tEX. \n\t2, 5 = GOOD\n\t5, 2 = BAD")
            else:
                print("\nYou did not enter a number.")
                print("Please make sure that you do not include decimals, and that it is a number.")
                print("\n\tEX. \n\t2 = GOOD\n\t2.5 = BAD\n\ta = BAD")

    #----->This part finds what message to give when they win (score)<-----
    def score(): #This is how it calculates which message to give
        if numberOfTries <= .25*scoreMultiplyer: #it is .25 times the multiplyer which means one try on really hard
            print("WOW WOW WOW WOW WOW WOW WOW!! YOU MUST BE SOOOOOOOOOOOOOOOOO LUCKY SINCE SOMEHOW IT ONLY TOOK YOU ", numberOfTries, "TRIES!!!!! WOW WOW WOW WOW WOW!!! YOU ARE UNOFFICIALLY THE BEST AT THIS GAME!!!!!!!")
        elif numberOfTries <= 1*scoreMultiplyer: #it is 1 times the multiplyer
            print("Wow!! That was mega super star amazing. It only took you", numberOfTries, "tries.")
        elif numberOfTries <= 2*scoreMultiplyer:
            print("That was amazing!! It only took you", numberOfTries, "tries.")
        elif numberOfTries <= 3*scoreMultiplyer:
            print("That was Good!! It took you", numberOfTries, "tries.")
        elif numberOfTries <= 4*scoreMultiplyer:
            print("That was ok, could be butter. It took you", numberOfTries, "tries.")
        elif numberOfTries <= 6*scoreMultiplyer:
            print("That was pretty bad... It sadly took you", numberOfTries, "tries.")
        else:
            print("I'm sorry about this, but I have to say the truth. You were terrible. It took you", numberOfTries, "tries.")

    #----->This part finds the multiplyer depending on how big the range is (to be more fair)<-----
    def scoreMultiplyerFunction(): #this changes the amount of tries to get different praise messages depending on how many possible values there are (difficulty)
        scoreMultiplyerCalc = upperNumber - lowerNumber #to find out how many possible solutions there are
        if scoreMultiplyerCalc <= 16: #if there is only 16 possible solutions
            scoreMultiplyer = 1
        elif scoreMultiplyerCalc <= 40: #if there is only 50 possible solutions
            scoreMultiplyer = 2
        elif scoreMultiplyerCalc <= 80:
            scoreMultiplyer = 3
        elif scoreMultiplyerCalc <= 300:
            scoreMultiplyer = 4
        elif scoreMultiplyerCalc <= 800:
            scoreMultiplyer = 5
        elif scoreMultiplyerCalc <= 2000:
            scoreMultiplyer = 6
        elif scoreMultiplyerCalc <= 10000:
            scoreMultiplyer = 10
        else:
            scoreMultiplyer = 12
        return(scoreMultiplyer) #returns it so that it can exist outside the function

    scoreMultiplyer = scoreMultiplyerFunction() #starts the function and assigns the scoreMultiplyer var to the result that is returned
    print("\n\n")

    #----->This part is the game itself<-----
    while complete == False:
        try: #it uses int, so if it errors out, then they did not enter an integer, so it will ask them to enter again
            numberOfTries += 1
            print("Pick a number between", lowerNumber, "and", upperNumber)
            numberGuess = int(input("--> "))
            if numberGuess > upperNumber: #if they guessed above the range
                numberOfTries -= 1 #needs to remove this since it did not actually count
                print("You guessed above the range. It has not been counted against your score.\n")
            elif numberGuess < lowerNumber: #if they guessed below the range
                numberOfTries -= 1 #needs to remove this since it did not actually count
                print("You guessed below the range. It has not been counted against your score.\n")
            elif numberGuess != number:
                if numberGuess > number: #to write whether or not they are above or below the number
                    print("You are too high\n")
                else:
                    print("You are too low\n")
            else:
                print("\n\nYay!! You guessed the number!!")
                score() #diaplays their score by running the score function
                complete = True
                playagainPrompt = input("\n\nDo you want to play again? --> ")
                try:
                    if playagainPrompt.lower().strip()[0] == "y" or playagainPrompt.lower().strip()[0] == "1":
                        playagain = True
                    else:
                        playagain = False
                        print("\n\n\tThank you for playing!!\n\tHave a great day!!\n")
                except (IndexError, ValueError):
                    playagain = False
                    print("Defaulting to No")
                    print("\n\n\tThank you for playing!!\n\tHave a great day!!\n")
        except (IndexError, ValueError): #if they did not enter an integer
            numberOfTries -= 1 #needs to remove this since it did not actually count
            print("You did not enter an integer, it has not been counted against your score.\n")
