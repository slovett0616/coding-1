import random

def dice_game():
    print("Welcome to the Dice Game")
    print("Roll a 7 to win. Roll anything else to lose.")
    score = 0
    
    while True:
        choice = input("Enter 'r' to roll or 'q' to quit: ")
        
        if choice == 'q':
            print(f"Thanks for playing. final score: {score}")
            break
            
        elif choice == 'r':
            roll = random.randint(1, 7)
            print(f" you rolled a {roll}")
            
            
            if roll == 7:
                score += 10
                print(f"You rolled a 7, you win! current score:{score}")
            else:
                score -= -5
                print(f"You lost, try again. Current score : {score}")
                
        else:
            print("This is not an input. Please enter 'r' or 'q'.")

dice_game()

# I had help for this i still dont really understand while loops n stuff