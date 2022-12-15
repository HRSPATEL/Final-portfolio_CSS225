# Harsh Patel
# Module 5 homework assignments
# 11/04/2022

# problem 1
# print Hello world 100 times using for loop


# for num in range(100):
#     print("hello World!")

# ==================== Problem 1 ends here


# problem 2
# using for loop to print each number and its square, each value on new line

# num_list = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#
# for i in num_list:
#
#     print("Square of",i,"is", i*i)

# ==================== Problem 2 ends here


# problem 3
# Using a for loop and turtle module for drawing triangle or square using user input

# This program is insprired from multiple stackoverflow answers, I understand most of it but the rest.
# I missed the class of week 5 hence took help of online resources
# the one feature I added of fill color, it instead change the color of the arrow
# refrence link: https://stackoverflow.com/questions/28356395/python-write-a-program-that-asks-the-user-for-a-color-a-line-width-a-line-len?newreg=c232419bb3aa437aab1218a75a486e84


# from turtle import Turtle, Screen, TurtleGraphicsError
#
# screen = Screen()
#
# length = None
# while not length:
#     length = screen.numinput('Select Length', 'Enter your desired line length:', minval=1)
#
# width = None
# while not width:
#      width = screen.numinput('Select Width', 'Enter your desired line width:', minval=1, default=1)
#
# turtle = Turtle()
# turtle.pensize(width)
#
# color = None
# while not color:
#     try:
#         color = screen.textinput('Select Color', 'Enter your desired line color:')
#         turtle.pencolor(color)
#     except TurtleGraphicsError:
#          color = None
#
# fill = None
# while not fill:
#     try:
#         fill = screen.textinput('Select fill Color', 'Enter your desired fill color:')
#         turtle.fillcolor(fill)
#     except TurtleGraphicsError:
#          fill = None
#
# shape = None
# while not shape or shape.lower() not in {'line', 'triangle', 'square'}:
#     shape = screen.textinput('Select Shape', 'Specify whether you want a line, triangle, or square:')
# shape = shape.lower()
#
# if shape == 'line':
#     turtle.forward(length)
# elif shape == 'triangle':
#     for _ in range(3):
#         turtle.forward(length)
#         turtle.right(120)
# else:
#     for _ in range(4):
#         turtle.forward(length)
#         turtle.right(90)
#
# screen.exitonclick()


# ==================== Problem 3 ends here



# problem 4
# printing 1 to 50 numbers. Numbers divisible by 3, 5 and/or both are distinguished


# for i in range(1,51):
#
#     if(( i%3 == 0) & ( i%5 == 0)):
#         print("divisible by both!")
#
#     elif (i%3==0):
#         print("divisible by 3")
#     elif(i%5==0):
#         print("divisible by 5")
#     else:
#         print(i)


# extra credit problem
# inspired but created from scratch


# import turtle
#
# pen=turtle.Turtle()
# pen.speed(1)
#
# pen.setheading(270)
# pen.begin_fill()
#
# # penguin body
# pen.circle(40,180)
# pen.forward(80)
# pen.circle(40,180)
# pen.forward(80)
# pen.end_fill()
#
# #Belly
# pen.fillcolor("white")
# pen.goto(10,0)
# pen.begin_fill()
# pen.circle(40)
# pen.end_fill()
#
# #Eyes
# pen.setheading(0)
# pen.goto(30,80)
# pen.begin_fill()
# pen.circle(20)
# pen.end_fill()
# pen.goto(70,80)
# pen.begin_fill()
# pen.circle(20)
# pen.end_fill()
#
# # Eyes dot
# pen.shape("circle")
# pen.fillcolor("black")
# pen.penup()
# pen.goto(30,100)
# pen.stamp()
# pen.goto(70,100)
# pen.stamp()
#
#
# #Nose
#
# pen.shape("triangle")
# pen.fillcolor("orange")
#
# pen.goto(50,70)
# pen.setheading(270)
# pen.stamp()
#
# #Flaps
# pen.fillcolor("black")
# pen.pencolor("white")
# pen.setheading(180)
# pen.goto(0,50)
# pen.stamp()
# pen.setheading(0)
# pen.goto(100,50)
# pen.stamp()
#
#
# #legs
# pen.shape("square")
# pen.fillcolor("orange")
# pen.goto(35,-50)
# pen.stamp()
# pen.goto(65,-50)
# pen.stamp()
# turtle.done()
#
#
# ================ extra credit problem ends here