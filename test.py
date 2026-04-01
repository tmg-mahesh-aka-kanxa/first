'''
a = "dsfg"
def x(a):
    b = input()
    print("inside",a)
    a = b
x(a)
print(a)
'''
c = ""
def dsf(x):
    g = "hallo world"
    global c
    c = g
    
dsf(c)
print(c)