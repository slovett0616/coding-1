import random

def dice_game():
    print("Welcome to the Dice Game")
    print("Roll a 7 to win. Roll anything else to lose.")
    
    while True:
        choice = input("Enter 'r' to roll or 'q' to quit: ")
        
        if choice == 'q':
            print("Thanks for playing")
            break
            
        elif choice == 'r':
            roll = random.randint(1, 7)
            print("You rolled a: {roll}")
            
            
            if roll == 7:
                print("You rolled a 7, you win!")
            else:
                print("You lost, try again")
                
        else:
            print("This is not an input. Please enter 'r' or 'q'.")

dice_game()

# I had help for this i still dont really understand while loops n stuff