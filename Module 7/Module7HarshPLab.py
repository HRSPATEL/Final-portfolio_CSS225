# Harsh Patel
# Module 7 problems
# please remove appropriate comments to active the code
# 12.02.2022

# ======================================== Problem 1 starts here

# import math
#
# r = int(input("please enter a number"))
# def area_of_circle(r):
#     area_of_circle = math.pi * r * r
#     return area_of_circle
#
# print(area_of_circle(r))

# ======================================== Problem 2 starts here

#Write a Python function to check whether a number is between 1 and 10. The
#function should take a number as a parameter and return True if the number is between 1 and
#10, and False if the number is not between 1 and 10

# n = int(input("please enter number "))
# def test_range(n):
#     if n in range(0,10):
#         print("True")
#     else :
#         print("False")
# test_range(n)


# ======================================== Problem 3 starts here

#Write a Python function to multiply all the numbers in a list. The function should
#take a list of numbers as a parameter and return the final result of the multiplication

# numbers = [8, 2, 3, 1, 8]
# def multiply(numbers):
#     total = 1
#     for x in numbers:
#         total = x * total
#     return total
# print(multiply(numbers))

# ======================================== Problem 4 starts here
# Write a Python function that takes a list of numbers and returns a new list with
# unique elements of the first list. Use the append() function

# numbers = [1, 3, 3, 3, 6, 2, 3, 5]
# def unique_list(numbers):
#     unique = []
#     for item in numbers :
#         if item not in unique:
#             unique.append(item)
#     return unique
#
# print(unique_list(numbers))


# ======================================== Problem 5 starts here
# four circles inside each other

# import turtle
# sz = 200
# def drawSquare(t, sz):
#
#     for i in range(16):
#         t.forward(sz)
#         t.left(90)
#         sz = sz - 10
#
#
# wn = turtle.Screen()
# alex = turtle.Turtle()
# alex.color("blue")
#
# drawSquare(alex, sz)
# wn.exitonclick()

# ======================================== Problem 6 starts here
# the car attributes
# class car:
#     def __init__(self, model, year, color, typee, manufacturer):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.typee = typee
#         self.manufacturer = manufacturer
#     def get_model(self):
#         return self.model
#     def get_year(self):
#         return self.year
#     def get_color(self):
#         return self.color
#
#     def get_typee(self):
#         return self.typee
#
#     def get_manufacturer(self):
#         return self.manufacturer
#     def fullspecs(self):
#         return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.typee + ' ' + self.manufacturer
# car1 = car("Sports", 2012, "Blue", "Sedan", "Honda")
# car2 = car("Sedan", 2020, "Black", "SUV", "GMC")
# print(car1.get_color())
# print(car1.get_model())
# print(car2.get_color())
# print(car1.get_typee())
# print(car2.get_manufacturer())
#
# print(car1.fullspecs())
# print(car2.fullspecs())

# =========================================== ends here