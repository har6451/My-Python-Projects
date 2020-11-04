# Dice Rolling Simulator

# Importing required Libraries
import random


def dice_roll():
    random_number = random.randint(1, 6)
    return random_number


def main():
    # Declaring variables
    player1 = 0
    player2 = 0
    rounds = 1
    player1wins = 0
    player2wins = 0
    while rounds != 11:
        print("Round " + str(rounds))
        player1 = dice_roll()
        player2 = dice_roll()
        print("Player 1 rolls " + str(player1))
        print("Player 2 rolls " + str(player2))
        rounds += 1

        if player1 == player2:
            print("Draw")
        elif player1 > player2:
            print("Player 1 wins")
            player1wins += 1
        elif player1 < player2:
            print("Player 2 wins")
            player2wins += 1

    if player1wins == player2wins:
        print("Drawn")
        print("Player 1 and Player 2 both won " + str(player1wins) + " rounds.")
    elif player1wins > player2wins:
        print("Player 1 won " + str(player1wins) + " rounds. Where Player 2 won just " + str(player2wins) + " rounds.")
        print("Player 1 won!!!!!")
    elif player1wins < player2wins:
        print("Player 2 won " + str(player2wins) + " rounds. Where Player 1 won just " + str(player1wins) + " rounds.")
        print("Player 2 won!!!!!")


main()
