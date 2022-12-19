# section_3

# Harsh Patel
# 11/12/2022

# section 3 of the game, where third scene takes place

import random
import time
import section_1
import combat

def start():
    print("You look for a weapon and find something\n")
    time.sleep(2)
    print("please press ENTER to find out what is your weapon(tool) you found\n")
    input()

# this random list will give you random weapon which you can use or may not
# if you don't get appropriate weapon, you have option to research for the weapon
# only a sharp stick will help you make lion go away

    weapons_list = ["stick", "rope", "piece_of_meat"]
    w1 = random.choice(weapons_list)
    print(w1, "is your tool/weapon")

    if (w1 == "rope"):
        print("You couldn't do much with rope")
        print("Lion grabs this opportunity and runs away with your loved pet... :(")

        choice5 = input("I am sorry, would you like to find weapon again? y/n \n")
        if (choice5 == "y" or choice5 == "Y"):
            start()
        else:
            print("Please try again next time, byeee!!")
            exit()

    elif (w1 == "piece_of_meat"):
        print("You throw away the meat to lure the lion away")
        print("Unfortunately")
        print("It wasn't big enough for lion and even not far away for you to have enough time")
        print("The lion takes your pet, :(")
        choice6 = input("I am sorry, would you like to find weapon again? y/n \n")
        if (choice6 == "y" or choice6 == "Y"):
            start()
        else:
            print("Please try again next time, byeee!!")
            exit()

    elif (w1 == "stick"):
        print("You found a sharp stick which can help you hurt lion")
        print("Now you have two options")
        choice7 = int(input("either   1. Attack or 2. Run away \n"))
        if choice7 == 1:
            combat.start()

        elif choice7 == 2:
            print("You run away")
            print("Since you had a sharp weapon on you, the lion didn't hurt you\n")
            print("but your beloved pet is lost")
            print("in a way, you lose the game :(")

            choice8 = input("I am sorry, would you like to restart the game? y/n ")
            if (choice8 == "y" or choice8 == "Y"):
                section_1.start()
            else:
                print("Please try again next time, byeee!!")
                exit()



