# I wasnt here thursday and i didnt know my login so its late.


def vending_Machine():
    B3 = "nachochips"
    G4 = "bbqchips"
    G7 = "plainchips"
    D3 = "water"
    G5 = "colasoda"
    Q = 'Quit'
    
    print("Please type in a Vending Machine number")
    
    userChoice = ""
    while userChoice != 'Q':
        print("Please enter an item code: ")
        userChoice = input()
        
        if userChoice == 'B3':
            print("Here are your Nachos")

        elif userChoice == 'G4':
            print("Here are your bbqchips")

        elif userChoice == 'G7':
            print("Here are your plainchips")

        elif userChoice == 'D3':
            print("Here is your water")
            
        elif userChoice == 'G5':
            print("Here is your cocacola")
            
        elif userChoice == 'Q':
            print("End")
            break

vending_Machine()