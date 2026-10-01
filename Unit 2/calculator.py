# FUNCTIONS ARE JUST CODE INSTRUCTIONS

# Phase 1 of function: function definition- actual code- does nothing
def calculate_add():
    print("Program has started: please type in 2 numbers to add" )
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("Program has ended.")

# Phase 2 of function: function call- actually runs and does something
calculate_add() 

# make a function for: 
# subtraction     
def calculate_subtract():
    print("Program started: type in 2 numbers to subtract" )
    num3 = int(input())
    num4 = int(input())
    print(num3 - num4)
    print("Program Done")
    
calculate_subtract()
# multiplication
def calculate_multiply():
    print("Program started: type in 2 numbers to multiply")
    num5 = int(input())
    num6 = int(input())
    print(num5 * num6)
    print("Program Done")
    
calculate_multiply()
# division
