#Module 5 Code examples

#The 'import' keyword allows us to use code found in other files (modules).
#All importing should be done at the very beginning of the file.

#The turtle module lets us draw simple shapes and lines to the screen.
import turtle


#******************************
#Lists
#
#A list is a group of data.
#For example, this is a list of colors inside a variable called 'colors'.
#The elements of a list MUST be separated by commas.
#Pay very close attention to where the commas and quotations are!
colors = ["red","blue","green","yellow"]
#The following line prints the first element in the list:
print(colors[1])
#Can you figure out how to print the second element in the list?

#******************************
#For loops
#
#A for loop repeats code a specific number of times.
#The following code prints each element in the colors list
for color in colors:
    #Each time the loop repeats, the value of the color variable will
    #change to the next string in the colors list
    print(color)

#If we want something to repeat a set number of times,
    #we can use the range() function.
#This code will print the numbers 1 through 10.
for num in range(1,11):
    print(num)

#******************************
#Turtles!
#
#This line creates a new turtle named Tom.
#We can theoretically create as many turtles as we want!
Tom = turtle.Turtle()

#The pencolor() function sets the color of the line our turtle will draw
Tom.pencolor("blue")
#The forward() function makes Tom draw a line
    #of some number of pixels in length.
#This line will draw a blue line 100 pixels long.
Tom.forward(100)

#To turn the turtle, use the left() or right() functions.
#This line will cause Tom to turn 45 degrees to the right,
    #and draw a line 200 pixels in length.
Tom.right(45)
Tom.forward(200)

#Let's draw a pentagon!
#This will draw a red pentagon with a blue outline.
Tom.fillcolor("red")
Tom.begin_fill()
for num in range(1,6):
    Tom.left(72)
    Tom.forward(200)
Tom.end_fill()


#******************************
#Modulus (%) operator
#The modulus operator lets us see if a number is evenly divisible by another.
#It performs a division, then gives us the remainder instead of the quotient.
number = int(input("What is your number?\n"))
if number % 4 == 0:
    print("Your number is divisible by 4!")
else:
    print("Your number is not divisible by 4!")





