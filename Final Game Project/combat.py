# main_c.py

# Harsh Patel
# 11/12/2022

import random
import time
import section_1
import main_character

class main_character():
    name = "Kanya"
    Health = 10
    attack = 5
    weapons_list = ["stick", "rope", "piece_of_meat"]
    medicine = []

# there is random attack generator which will decide if you should attack or back off

def start():
    print("You attack lion and guess what...")
    print("Your sharp tool indeed worked and did some injuries to lion")
    print("press ENTER to continue...")
    input()

    random_attack = ["Lion attacks you", "Lion backs off"]

    r1 = random.choice(random_attack)

    if (r1 == "Lion attacks you"):
        print("Lion attacks you")

        c4 = input("press 'y' to attack lion")
        if (c4 == "y"):
            print("Lion backs off")
            time.sleep(2)
            print("Hoorah! You save your pet  (press enter)")
            input()
            print("You win!!!")
            time.sleep(2)
            print("Thank you for playing")
            time.sleep(3)
            print("More features and complexity yet to come, stay tuned on github for more updates about the game")
            time.sleep(1)
            print("https://github.com/HRSPATEL/Final-portfolio")
            exit()

        else:
            print("Lion attacks you again...")
            time.sleep(2)
            print("You are severely injured")
            time.sleep(2)
            print("The lion runs away with your pet in mouth")
            time.sleep(1)
            print("You lose game :(... Sorry!!!")
            time.sleep(3)

            choice2 = input("Would you like to try again? Y/N")
            if (choice2 == "y" or choice2 == "Y"):
                section_1.start()
            else:
                print("Please try again next time, byeee!!")
                exit()




    elif (r1 == "Lion backs off"):
        print("Lion backs off")
        time.sleep(2)
        print("Hoorah! You save your pet  (press enter)")
        input()
        print("You win!!!")
        time.sleep(2)
        print("Thank you for playing")
        time.sleep(3)
        print("More features and complexity yet to come, stay tuned on github for more updates about the game")
        time.sleep(1)
        print("https://github.com/HRSPATEL/Final-portfolio")
        exit()


