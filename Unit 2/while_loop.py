# Loop - a loop is a construct (special function) that repeats itself. 
# In programming, a loop allows to repeat code instructions.

# There are two types of loops: For loop and While loop

# While loop - a type of loop where so long as a condition is equal
# to true it will keep running "forever"

# The keyword is while --> do while

# syntax
# num = 4
# while 2+2 == num: # Condition --> operations - must be TRUE
    # print("the program is running...")


# While Loops will ALWAYS run unless you change the condition!
# we can do this by writting intructions to manually change it.
# The computer must ALWAYS complete their tasks before moving to the next step.


def guessingGame():
    correctAnswer= 8
    attempts= 0
    print("WELCOME TO THE GUESSING GAME")
    print("Please type in a number between 1 and 10")
    userGuess = int(input("Please type in a number: "))
    while userGuess != correctAnswer:
        print("Sorry, incorrect. Guess again.")
        attempts+= 1
        print("attempts")
        userGuess =int(input("please try another number: "))
    print("Congrats! you guessed correctly. game over")
guessingGame()








# Question 1
# password reset function. Your function should take in a 
# user password as an input. within the function there should be a
# variable that contains the correct password.
# the user should be able to attempt to enter the password 4 times.
# On the fourth attempts of getting the password incorrect,
# it should print out a message telling the user that
# their account has been locked. If the user gets the password
# correct it should print out a message telling them
# they can access their account.


def PasswordReset():
    correctAnswer= 9872
    attempts= 4
    print("Welcome to the PasswordReset ")
    userGuess = (input("Please type in your current password: "))
    while userGuess != correctAnswer and attempts == 4:
        print("Incorrect Password.")
        attempts-= 1 
        print("attempts left:" + str(attempts))
        userGuess =(input("Try Again: "))
    print("You have been locked out of your account.")
    
    print("You can now access your account.")
PasswordReset()
























    