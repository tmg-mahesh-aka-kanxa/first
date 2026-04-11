print("Welcome to my calculater")
print("You can calculate here 2 numbers")
first_num = int(input("Enter your first number : "))
task = input("What do you want to do '+' or '-' or '*' or '/' :")
second_num = int(input("Enter your second number : "))
emogi = str("('_')")
class Calculater:
    def __init__(self,first,second):
        self.first = first
        self.second = second
    
    def addition(self):
        return self.first + self.second
        
    
    def substraction(self):
        return self.first - self.second
    
    def multiplacation(self):
        return self.first * self.second
    
    def devision(self):
        return self.first / self.second

my_calculate = Calculater(first_num,second_num)

try :
    if "+" in task :
        print(my_calculate.addition())
        
    if "-" in task :
        print(my_calculate.substraction())
        
    if "*" in task :
        print(my_calculate.multiplacation())
        
    if "/" in task :
        print(my_calculate.devision())
        

except TypeError:

  print("An exception occurred")


# except:
#     print(f"Please enter valid input {emogi}")