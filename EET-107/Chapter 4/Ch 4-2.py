#Sean Kelley
#Lab 4.2
#25 June 2021

import turtle
line_amount = int(input("Please enter the number of lines in the pyramid (1-10): "))
line_distance = 25
lines_printed = 2
line_distance_back = 20
t = turtle.Turtle()
t.speed(1)
endflag = False
while endflag == False:
    while lines_printed <= line_amount:
        lines_printed += 1
        line_distance += 20
        t.forward(line_distance)
        t.penup()
        t.right(90)
        t.forward(20)
        t.left(90)
        t.forward(line_distance_back)
        line_distance_back += 22
        t.pendown()
        t.backward(line_distance * 2)
        while line_amount <= 0 or line_amount > 10:
            line_amount = int(input("Please enter a value between 1 and 10: "))
    draw_another = input("Would you like to draw another triangle (Y or N): ")
    if draw_another = "N":
        endflag = True
