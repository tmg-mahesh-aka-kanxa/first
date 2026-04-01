'''
scissor = 1
paper = 2
rock = 3
'''
scissor = "scissor"
paper = "paper"
rock = "rock"
playagain = "sadf"

import random
def mygame():
    print("WELCOME TO MY SCISSOR PAPER ROCK GAME !!!!!!!!")

    userinput = input("Enter your choice :-- ")

    bot = random.choice(["rock","paper","scissor"])
    print("Bot chose :-- ",bot)

    if(userinput == bot) :
        print("TIE !!!!!!!")

    elif(bot == scissor and userinput == rock or bot == rock and userinput == paper or bot == paper and userinput == scissor):
        print("(°_°) YOU WIN !!!!!!!!")

    elif(userinput == rock and bot == paper or userinput == paper and bot == scissor or userinput == scissor and bot == rock):
        print("(°n°) YOU LOSE !!!!!!!!!")

    else :
        print("invalid input")

    print("Press enter to play again")
    playagain = input()




while playagain == "":
    mygame()