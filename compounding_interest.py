import math

user_choice = int(input("Input 1 for compound amount or 2 for compound interest : "))
capital = int(input("Input capital : "))
percent = int(input("Input interest percent % :"))
year    = int(input("Input years :"))

def compound_interest():
    a = 1 + (percent / 100)
    b = pow(a,year)
    c = b - 1
    d = capital * c
    return c

def compound_amount():
    a = 1 + (percent / 100)
    b = pow(a,year)
    d = capital * b
    return d


if (user_choice == 1):
    print(compound_amount())

if (user_choice == 2):
    print(compound_interest())

