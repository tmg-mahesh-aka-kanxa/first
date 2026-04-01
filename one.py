'''
scissor = 1
paper = 2
rock = 3
'''
import random

print("WELCOME TO MY SCISSOR PAPER ROCK GAME !!!!!!!!")
print("Chose 1 for scissor or 2 for paper or 3 for rock")

userinput = int(input("Enter your choice :- ",))

bot = random.randint(1,3)
print("Bot chose ",bot)

if(userinput == bot) :
    print("TIE !!!!!!!")

elif(bot == 1 and userinput == 2 or bot == 2 and userinput == 1 or bot == 3 and userinput == 1):
    print("YOU LOSE !!!!!!!!")

elif(userinput == 1 and bot == 2 or userinput == 2 and bot == 1 or userinput == 3 and bot == 1):
    print("YOU WIN !!!!!!!!!")

else :
    print("invalid input")