"""
     *
    ***
   *****
  *******
 *********
***********

 *
***

"""


i = int(input())
a = 0
b = 1
x = (i * 2) 
c = int((x/2)-1)
d = input("symbol : ")

while a < i:
    # print( "_"*c +  "*" * b)
    print(" " * c, end= "" ) 
    print( d * b)
    a += 1
    b += 2
    c -= 1