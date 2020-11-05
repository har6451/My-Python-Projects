# Rock Paper Scissor Game

import random


def rockpaperscissor():
    print("Rock Paper Scissor")
    print("1. Rock\t  2. Paper\t 3. Scissor")

    weapons = ['Rock', 'Paper', 'Scissor']

    computer_count = 0
    your_count = 0
    repetition = 10
    while repetition > 0:
        random_number = random.randint(1, 3)
        your_choice = random.randint(1, 3)
        if random_number == your_choice:
            print(f"You and Computer both picked {weapons[random_number - 1]}")
            print("Match Draw")
        if random_number == 3 and your_choice <= 2:
            print(f"Computer picked {weapons[random_number - 1]}")
            print(f"You picked {weapons[your_choice - 1]}")
            print(f"Computer Won!")
            computer_count += 1
        if random_number <= 2 and your_choice == 3:
            print(f"Computer picked {weapons[random_number - 1]}")
            print(f"You picked {weapons[your_choice - 1]}")
            print(f"You Won!")
            your_count += 1
        if random_number == 2 and your_choice == 1:
            print(f"Computer picked {weapons[random_number - 1]}")
            print(f"You picked {weapons[your_choice - 1]}")
            print(f"Computer Won!")
            computer_count += 1
        if random_number == 1 and your_choice == 2:
            print(f"Computer picked {weapons[random_number - 1]}")
            print(f"You picked {weapons[your_choice - 1]}")
            print(f"You Won!")
            your_count += 1
        print(f"Your Score: {your_count}")
        print(f"Computer Score: {computer_count}")
        repetition -= 1
    if your_count > computer_count:
        print(f"You Won!\t Computer won only {computer_count}")
    elif your_count == computer_count:
        print(f"Match Draw\t Both won {computer_count}")
    else:
        print(f"Computer Won!\t You won only {your_count}")


rockpaperscissor()
