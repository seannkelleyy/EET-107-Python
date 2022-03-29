#Sean Kelley
#Chapter 3 Lab 3
#19 June 2021

shape_choice = input("Do you wish to create a (c)ircle, (s)quare, or a (t)riangle?: ")
size_choice = int(input("What size would you like the shape to be (1-300)?: "))
while shape_choice != "c" and shape_choice != "s" and shape_choice != "t":
    shape_choice = input("Invalid input. Please input (c), (s), or (t): ")
while size_choice > 300 or size_choice < 1:
    size_choice = int(input("Invalid input. Please enter a value between 1 and 300: "))
import turtle
bob = turtle.Turtle()
bob.color("cyan")
bob.speed(1)
bob.begin_fill()
bob.shape("turtle")
if shape_choice == "c":
    bob.circle(size_choice / 2)
if shape_choice == "s":
    bob.forward(size_choice)
    bob.left(90)
    bob.forward(size_choice)
    bob.left(90)
    bob.forward(size_choice)
    bob.left(90)
    bob.forward(size_choice)
if shape_choice == "t":
    bob.forward(size_choice)
    bob.left(135)
    bob.forward(size_choice)
    bob.left(90)
    bob.forward(size_choice)
    bob.left(135)
    bob.forward(size_choice)
else:
    print("Invalid input")
bob.end_fill()
turtle.Screen().exitonclick()

