# Module 6 all in one labs
# Harsh Patel

# 11.24.2022

# problem 1 starts here
# Use a for loop and random.randrange to print 10 random integers between
# 25 and 35

# import random
# for i in range(0, 10):
#
#     print(random.randrange(25,35))

# ========================================== problem 2 starts here
# Use random.randrange to print an odd integer between 0 and 100

# import random as rn
# a = rn.randrange(0,100,2)
# b = a + 1
# print (b)

# ======================================== problem 3 starts here

# Use random.choice to select a day of the week from a list and print that day

# import random
#
# weekdays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
# print(random.choice(weekdays))


# ======================================== problem 4 starts here

# Write a program that will compute the area of a circle. Prompt the user to enter the radius and
# print a nice message back to the user with the answer

# import math
#
# r = float(input("Please enter the radius = "))
#
# area = math.pi * r * r
#
# print("Area of radius", r,"is", area,"squared")


# ======================================== problem 5 starts here
# Pythagorean theorem using the sqrt() and pow() functions


# import math
#
# a = float(input("enter a = "))
#
# b = float(input("enter b = "))
#
# print("C is ", math.sqrt((math.pow(a, 2)+math.pow(b, 2))))


# ======================================== problem 6 starts here
# factorial using for loop function


# num = int(input("Enter a number: "))
# factorial = 1
#
# if num < 0:
#    print("Sorry, factorial does not exist for negative numbers")
# elif num == 0:
#    print("The factorial of 0 is 1")
# else:
#    for i in range(1,num + 1):
#        factorial = factorial*i
#
# print("The factorial of",num,"is",factorial)

# ======================================== problem 6.2 starts here
# factorial using math function

# import math
#
# n = int(input("enter number "))
#
# print("factorial is ", math.factorial(n))