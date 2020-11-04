# Number Guessing

# Importing Libraries
import random

# Generating a random number
lower = int(input("Enter Lower Value: "))
upper = int(input("Enter Upper Value: "))

# Declaring Variables
count = 1
chance = 3

random_number = random.randint(lower, upper)
print("You have "+ str(chance) + " chances.")

while True:
    if count > 3:
        print("The number is " + str(random_number) + ".")
        print("Better luck next time!")
        break

    guess = int(input("Enter Your Guess: "))

    if guess != random_number:
        count += 1
        chance -= 1
        print("You have " + str(chance) + " chances left.")

    elif guess == random_number:
        print("You guessed it right in " + str(count) + " times.")
        break

    elif guess > upper:
        print("You guessed too high!")

    elif guess < lower:
        print("You guessed too small!")
