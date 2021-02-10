"""
This is just a program that I made when I thought of an old number guessing game that I played once.
Programmed by TheRuntingMuumuu
"""
#Just defining some variables
complete = False
numberGuess = 0 #Defining base values
numberOfTries = 0
scoreMultiplyer = 1

import random #needed for the random number generator
import os #needed to clear the screen
def clearScreen(): #clears screen
    if os.name == 'nt': #is it windows
        os.system('cls') #windows clear
    else:
        os.system('clear') #macos/linux clear

#figuring out the range and then picking a number
rules = input("Welcome to the Number Guessing Game. Do you want to see the rules? --> ") #assignes rules variable to the input from the user
if rules.lower().strip()[0] == 'y' or rules.strip()[0] == "1": #it checks if the first letter of the var rules is y, or 1
    print("rules to come")
    input("Press ENTER to continue -->")

#finds out the range and then the number
lowerNumber = int(input("\n\nWhat is the lower value for the range --> "))
upperNumber = int(input("What is the upper value for the range --> "))
number = random.randint(lowerNumber, upperNumber) #picks the number

def score(integer): #This is how it calculates which message to give
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

def scoreMultiplyerFunction(): #this changes the amount of tries to get different praise messages depending on how many possible values there are (difficulty)
    scoreMultiplyerCalc = upperNumber - lowerNumber
    if scoreMultiplyerCalc <= 16: #if there is only 16 possible solutions
        scoreMultiplyer = 1
    elif scoreMultiplyerCalc <= 50: #if there is only 50 possible solutions
        scoreMultiplyer = 2
    elif scoreMultiplyerCalc <= 100:
        scoreMultiplyer = 3
    elif scoreMultiplyerCalc <= 500:
        scoreMultiplyer = 4
    elif scoreMultiplyerCalc <= 1000:
        scoreMultiplyer = 5
    else:
        scoreMultiplyer = 6
    return(scoreMultiplyer) #returns it so that it can exist outside the function

scoreMultiplyerCalc = upperNumber - lowerNumber #to find out how many possible solutions there are
scoreMultiplyer = scoreMultiplyerFunction() #starts the function and assigns the scoreMultiplyer var to the result that is returned
clearScreen()

while complete == False:
    numberOfTries += 1
    print("Pick a number between", lowerNumber, "and", upperNumber)
    numberGuess = int(input("--> "))
    if numberGuess != number:
        if numberGuess > number: #to write whether or not they are above or below the number
            print("You are too high\n")
        else:
            print("You are too low\n")
    else:
        print("\n\nYay!! You guessed the number!!")
        score(scoreMultiplyer)
        complete = True