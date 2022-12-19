# main_game.py

# Harsh Patel
# 11/12/2022

# the main_game file that controls everything

# the file has time sleep function so please play it slowly or it might crash with wrong input
# Also There is only one particular way in the section2 to win so keep you eyes on
# ANSWERS TO WIN: keep trying by saying yes, eventually the random will throw you good tools to win
#               : perhaps good chance to win


# all required imports are here
import main_character
import section_1
import section_2
import section_3
import combat
import time


# start of game
print("""Hi there, welcome to a typical jungle in a tropical country
A girl living in a village near the jungle needs your help
Do you mind helping her?!""")
time.sleep(1) # the sleep timer you will see through out the game


print("press any key to continue the game...")

input() # will take any input and start the game

section_1.start()












