import random

def RockPaperScissors():
    score = 0
    bot_Score = 0
    rounds = 0
    
    print("Welcome to RockPaperScissors")
    print("Enter r, p, or s to play. Beat the bot to win points")
    
    while True:
        if rounds == 3:
            print("You lose")
            print(f"Final Score. You: {score} points | bot: {bot_Score} points")
            break

        choice = input("Enter 'r' for rock, 'p' for paper, 's' for scissors or 'q' to quit: ")
        
        if choice == 'q':
            print(f"Your final score is: {score} points. bot score: {bot_Score} points.")
            break
            
        elif choice == 'r' or choice == 'p' or choice == 's':
            roll = random.randint(1, 3)
            
            if roll == 1:
                cpu_choice = 'r'
                print("CPU chose: rock")
            elif roll == 2:
                cpu_choice = 'p'
                print("CPU chose: paper")
            else:
                cpu_choice = 's'
                print("CPU chose: scissors")
            
            if choice == cpu_choice:
                print(f"Tie Current score: {score}")
            elif (choice == 'r' and cpu_choice == 's') or (choice == 'p' and cpu_choice == 'r') or (choice == 's' and cpu_choice == 'p'):
                score += 1
                print(f"You win and gained +1 point. Current score: {score}")
            else:
                cpu_score += 1
                print(f"You lose and the bot wins +1 point. Current score: {score}")
                
            rounds += 1
                
        else:
            print("You cant use this. Please enter 'r', 'p', 's' to play or 'q' to quit.")

RockPaperScissors()




