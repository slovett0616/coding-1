# Scenario Activity: what operator family is being used and what operator symbol are you using?

# Scenario 1.) Arithmetic Operator because its calculating balances
# Scenario 2.) Logical Operator because both conditions need to be true
# Scenario 3.) Logical Operator because they are checking if the contact numbers work
# Scenario 4.) Comparisson Operator because its checking if there was 100$ spent or not
# Scenario 5.) Arithmetic Operator because they are calculating a 7% tax to 200$ shoes

# Assignment Scenarios:


print(200== 100)  # False
print(13 > 18) # False 
print("Coding 1"== "coding1") # False
print(0 != 0) # False

# A cash register program that needs to calculate 
# the final balance of two items.

book = 10.99
tablet = 399.99

print(book + tablet)

# A program checking if you have spent over 100 dollars before giving you a discount.

cart= 98.87
amounterToGetDiscount= 100.00

print(cart > amountToGetDiscount)

# A program that applies 7% sales tax to your 200$ dollar shoes

Shoes = 200.00
Tax = 0.07

print(Shoes * Tax)

# A college app program that checks if GPA is above 85 and that you have a letter of recommendation to admit you in.

GPA = 86
Recommendation = True

print(GPA > 85 and Recommendation == True)

# A school safety program that checks if at least 1 of 2 emergency contact numbers works.

parentContact1 = False  
parentContact2 = True 

print(parentContact1 == True or parentContact2 == True)