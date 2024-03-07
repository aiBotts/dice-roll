import random

# This program asks a user to roll the dice, displays the result of the dice values until the user
# calls it quits for the  night

# Give the program a title
print()
print("*******Welcome to Big Money Dice Rollers!*******")
print()


# Defining the main() function
def main():
    new_player = input("Do you want to roll the dice? (y/n): ")
    while new_player == "y":
        roll_dice()                                                      # Calling the roll dice function
        print()
        new_player = input("Roll again? (y/n): ")
        if new_player != 'y':
            print("Thank you for playing, Goodbye!")
        else:
            continue


# Creating the value for a single die roll
def roll():
    roll1 = random.randint(1, 6)
    return roll1


# defining the sum of two dice rolls together
def roll_dice():
    die1 = roll()
    die2 = roll()
    print("Die 1: ", die1)
    print("Die 2: ", die2)
    sum_dice = die1 + die2

    # Creating an if/else statement for the custom rolls
    if die1 == 1 and die2 == 1:
        print("Total: ", sum_dice)
        print("Two ones (Snake Eyes!)")
    elif die1 == 6 and die2 == 6:
        print("Total: ", sum_dice)
        print("Two sixes (Boxcars!)")
    elif die1 == 4 and die2 == 4:
        print("Total: ", sum_dice)
        print("Two 4s (Square Pair!)")
    elif die1 == 2 and die2 == 2:
        print("Total: ", sum_dice)
        print("Two 2s (Ballerina!)")
    else:
        print("Total: ", sum_dice)



# Calling the main function
main()
