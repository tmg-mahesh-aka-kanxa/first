'''
scissor = 1
paper = 2
rock = 3
'''
one = "scissor"
two = "paper"
three = "rock"

import random

print("WELCOME TO MY SCISSOR PAPER ROCK GAME !!!!!!!!")

userinput = input("Enter your choice :-- ")

bot = random.choice(["rock","paper","scissor"])
print("Bot chose :-- ",bot)

if(userinput == bot) :
    print("TIE !!!!!!!")

elif(bot == one and userinput == two or bot == two and userinput == one or bot == three and userinput == one):
    print("YOU LOSE !!!!!!!!")

elif(userinput == 1 and bot == two or userinput == two and bot == one or userinput == three and bot == one):
    print("YOU WIN !!!!!!!!!")

else :
    print("invalid input")