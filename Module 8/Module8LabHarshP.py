# Harsh Patel
# 12.01.2022
# Module 8 all problems

# ============================================= Problem 1 starts here

# Write a function that takes two inputs from a user and prints whether they are
# equal or not

# def checkEqual():
#   a = int(input("Enter a number: "))
#   b = int(input("Enter second number: "))
#   if a == b:
#     print("Numbers are equal")
#   elif a != b:
#     print("Numbers are not equal")
# checkEqual()

# ============================================= Problem 2 starts here
# Write a function that takes two inputs from a user and prints whether the sum is
# greater than 10, less than 10, or equal to 10

# def sum_ten():
#     a = int(input("Enter a number: "))
#     b = int(input("Enter second number: "))
#     x = a + b
#     if x == 10:
#         print("equal to 10")
#     elif x < 10:
#         print("less than 10")
#     elif x > 10:
#         print("greater than 10")
# sum_ten()

# ============================================= Problem 3 starts here
# Write a function that takes a list and prints if the value 5 is in that list

# def check5(lst):
#   if 5 in lst:
#     print('Number 5 is in the list')
# check5([2, 6, 8, 4, 5, 4, 2])



# ============================================= Problem 4 starts here
#Write a function that takes a year as a parameter and returns True if the year is a
#leap year, False if it is otherwise

# def leapYear():
#     year = int(input("Please enter year "))
#     if (year % 4) == 0:
#         if (year % 100) == 0:
#             if (year % 400) == 0:
#                 print(year," is a leap year")
#             else:
#                 print(year," is not a leap year")
#         else:
#             print(year," is a leap year")
#     else:
#         print(year,"is not a leap year")
#
# leapYear()


# ============================================= Problem 5 starts here
# 3 tasks to add to a game code
# I took help of online resources to put together a working code

# class character:
#     def __init__(self, nickname, weapons, weaknesses):
#         self.nickname = nickname
#         self.weapons = weapons
#         self.weaknesses = weaknesses
#
#     def get_model(self):
#         return self.nickname
#
#     def get_year(self):
#         return self.weapons
#
#     def get_color(self):
#         return self.weaknesses
#
#     def profile(self):
#         return self.nickname, self.weapons, self.weaknesses
#
#     def checks(self, p):
#         print("function works properly")
#         task = input("What task the character are going to perform(Write,climb,cook)")
#
#         # cooking
#         if task == "cook":
#             if p.weaknesses == "small":
#                 print("The character can not cook")
#
#             elif ('pan' in p.weapons) and ('groceries' in p.weapons):
#                 print("The character can cook")
#
#             else:
#                 print("The character will not Cook")
#
#
#         # climbing
#         elif task == "climb":
#             if p.weaknesses != "slow":
#                 print("The character can not climb the mountain")
#
#             elif ('rope' in p.weapons) and ('coat' in p.weapons) and ("first aid kit") in p.weapons:
#                 print("The character can climb")
#
#             else:
#                 print("The character will not climb a mountain")
#
#         # writing
#         elif task == "write":
#             if p.weaknesses != "confusion":
#                 print("The character can not write a book")
#
#             elif ('pen' in p.weapons) and ('paper' in p.weapons) and ("idea") in p.weapons:
#                 print("The character can a write a book")
#
#             else:
#                 print("The character will not write a book")
#
#
# player1 = character('', '', '')
# player1.nickname = 'Dragon Slayer'
# player1.weapons = ['pan', 'paper', 'idea', 'rope', 'groceries']
# player1.weaknesses = ['slow']
# for item in player1.weapons:
#     print("Item: ", item)
#
# for debuff in player1.weaknesses:
#     print("Debuff: ", debuff)
#
# player1.checks(player1)