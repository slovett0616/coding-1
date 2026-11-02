# What is a Loops --> Code that repeats.

# While loops = a block code that repeats itself until triggering
# condition is no longer TRUE. CAN BE INFINITE

# For loops = a type of loop (code block that repeats itself) BUT
# it only repeats itself up to a certain number of times.
# IT IS FINITE

# THINK OF FOR LOOPS AS THE COUNTING LOOP = for --> 4 = number of loop

# FOR LOOP SYNTAX
# "I" stands for itertator = programmers decided make this universal
# symbol for a placeholder for counting

for i in range(1, 5):  # "For i in" is all you need to make a For Loop. You can change "i" to anything you like
    print(i)  

for i in "school":
    print(i)

#LTST --> A collection type that acts as a container for 
# multiple data types and pieces of data.

# List Syntax
# A list is written like a variable BUT after the equal assignment
# symbol we use SQUARE BRACKETS and put all of the datas inside of 
# them.

fooditem1= "popcorn" # we can only store 1 piece of data in 1 variable

groceryList = ["popcorn", "apples", "water", "chips", "fish" , "celery"]


for groceryItem in groceryList: 
    print("I need to buy" + str(groceryItem))

itemPrices = [10.00, 20.00, 13.25, 7.95, 349.00]
tax = 0.07

for cost in itemPrices:
    # I want to know how much in taxes i need to pay on each item
    print(tax * cost)

semesterGrades = [90, 100, 78, 76, 74, 82, 84]  # "I" is the actual value inside of the list

for grade in semesterGrades:
    # I want to find ALL the grades lower than 85
    if grade < 85:
        print(grade)

# List are collection types for storing multiple pieces of data.
# Key elements and purposes for lists:
# List are organized and structured
# List can be manipulated and modified - mutable(means changeable)
# List items are accessible and usable

# When we want to access an item in a list, we use the indexing system.
# every item in a list is numbered.
# a list index always starts at zero(0)

#ex:
inventory= ['sword' ,'shield' , 'healing potion' , 'armor']

print(inventory[0]) #indicates that im going to the first position in the list

# When we want to add an item to our list, we use the append() method

#inventory.append('knife')
#print(inventory)






# Use a method to remove the healing potion from the list:
inventory.remove('healing potion')
print(inventory)

# use a method to add a 'warhammer' to the end of the list
inventory= ['sword' ,'shield' , 'healing potion' , 'armor']
weapon= ['warhammer']

inventory.extend(weapon)
print(inventory)


# Use a method to add a new 'healing potion' to index 4 of the list
inventory.insert(4, 'healing potion')
print(inventory)