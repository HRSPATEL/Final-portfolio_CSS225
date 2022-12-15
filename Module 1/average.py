# average.py

# Harsh Patel
# 10/04/2022

# the program asks for 3 inputs and gives us the average of those 3 numbers as output

# There was a lack of proper comments in the program

# The output extends for 15 places after the decimal, could be shortened, not necessary

round1 = int(input("Enter score for round 1: "))
round2 = int(input("Enter score for round 2: "))
round3 = int(input("Enter score for round 3: "))
average = (round1 + round2 + round3) / 3
print("the average score is: ", average)
