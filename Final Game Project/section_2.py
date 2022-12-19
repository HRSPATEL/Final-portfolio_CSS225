# section_2.py

# Harsh Patel

# 11/12/2022

# same goes for this one, imported required modules
import section_1
import section_3
import time
import main_character
import random




def start():
    print("You hear your pet in distance, You follow the lead")
    time.sleep(2)

    print("And you see what")
    time.sleep(3) # extra time for suspense
    print("a Lion standing right on your pet, trying to consume it...")
    time.sleep(2)

    print("What do you do to save your pet?")

# HINT: only the second option will let you win the game
    choice = int(input(""""
    1. Run away to save your life
    2. Look for a weapon to fight with the lion
    3. Climb on a tree and shout for villagers \n"""))


# rest is kind of same


    if choice == 1:
        print("You run away to save your life\n")
        time.sleep(2)
        print("But your pet is lost, You LOSE the game since it was a mission to save the pet\n")
        time.sleep(2)
        print("Try again next time...")
        time.sleep(2)
        choice2 = input("Would you like to try again? Y/N\n")
        if (choice2 == "y" or choice2 == "Y"):
            section_1.start()
        else:
            print("Please try again next time, byeee!!")
            exit()


    elif choice == 2:
        section_3.start()


    elif choice == 3:
        print("You climb on tree and shout for villagers...\n")
        time.sleep(2)
        print("NoOne really responds, the lion runs away with your pet...")
        time.sleep(1)
        print("Sorry   :(")
        choice9 = input("Would you like to try again? Y/N\n")
        if (choice9 == "y" or choice9 == "Y"):
            section_1.start()
        else:
            print("Please try again next time, byeee!!")
            exit()

