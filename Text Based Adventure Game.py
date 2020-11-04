# Text Based Adventure Game

while True:
    answer = input("What do you like to play? (yes/no) ").lower().strip()
    if answer == 'yes':
        answer = input("You reach a crossroads, would you like to go left or right? ").lower().strip()
        if answer == 'left':
            answer = input("You encountered a monster, would you like to run or attack? ")
            if answer == 'attack':
                print("This is not the greatest idea. You lost!")
            else:
                print("Good choice, You made it away safely.")
                answer = input("You see a car and plane. Which would you like to take? (car/plane) ").lower().strip()
                if answer == 'plane':
                    print("Unfortunately you do not know how to fly... Game over! You lost!")
                elif answer == 'car':
                    print("You won!")
                else:
                    print("Invalid Input")
        elif answer == 'right':
            answer = input("You saw an accident? Would you like to help or run? ").lower().strip()
            if answer == 'help':
                print("That's so nice, You won!")
            elif answer == 'run':
                print("You could help him but you didn't. You lost!")
            else:
                print("Invalid Input")
        else:
            print("Invalid Choice! You lost!")

    else:
        print("That's too bad!")
        break