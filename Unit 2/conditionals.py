# Conditional if/else logic- these are keywords that instruct your
# program to do specific instructions based on specific data
# or conditions

# conditional syntax (how it is written)
bill_amount = int(input("Type in a bull tender (1s, 5s, or 10s): "))

# If usually indicates that something is a possible option
if bill_amount == 1:
    print("Here are 4 quaters")
# elif allows us to indicate that there are more possible options
# you can have as many elif as you want
elif bill_amount == 5:
    print("here are 20 quaters")
elif bill_amount == 10:
    print("here are 40 quaters")

elif bill_amount == 20:
    print("Sorry we dont accept 20s")
# else is ALWAYS your last option

else:
    print("Sorry that type of bill is not accepted.")



def college():
    grade= int(input("Please type in your grade:"))
    if grade > 90:
        TempleU()
    else:
        ccp()
def TempleU():
    print("Congrats you meet the requirements for TempleU")
    print("238293")

def ccp():
    print("It looks like your GPA does not meet requirements BUT you can apply your CCP code")
    print("a7ds78sd")

college()

            
def calculate_add():
    print("Program has started: please type in 2 numbers to add" )
    num1 = int(input())
    num2 = int(input())
    print( num1 + num2)
    print("Program has ended.")



def calculate_subtract():
    print("Program started: type in 2 numbers to subtract" )
    num3 = int(input())
    num4 = int(input())
    print(num3 - num4)
    print("Program Done")



def calculate_multiply():
    print("Program started: type in 2 numbers to multiply")
    num5 = int(input())
    num6 = int(input())
    print(num5 * num6)
    print("Program Done")



def MainCalculator():
    print("MainCalculator is running")
    selection =int(input())
    if selection == 1: 
        calculate_add()
    elif selection == 2:
        calculate_subtract()
    elif selection == 3:
        calculate_multiply()
    else: 
        print("ERROR")
MainCalculator()
    
    
def Movie_Ticket_Prices():
    age = int(input("program started: please type in your age (7, 8 to 20 ,21 to 60, or 61): "))
    if age < 7:
        print("That will be 8$")
    elif age >= 8 and age<= 20:
        print("That will be 12$")
    elif age >= 21 and age <= 60:
        print("That will be 20$")
    elif age >= 61:
        print("You can watch for free")
    else:
        print("Sorry, but we cant accept this")
Movie_Ticket_Prices()
    

