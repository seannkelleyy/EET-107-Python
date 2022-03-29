#Sean Kelley
#Chapter 7-2
#11 July 2021

import time
from random import randint
print('*** Turtle Races ***\n')
def player_1_times():
    any_key = input("Player 1 press any key when you're ready to begin")
    print('Player 1 type the number shown as quickly as possible')
    start_time = time.time()
    count = 0
    while count < 4:
        count += 1
        for i in range(0, 3):
            random_num = randint(0, 9)
            plyr_1_inpt = int(input(f'Type {random_num}: '))
            if plyr_1_inpt == random_num:
                count += 1
                continue
            else:
                while plyr_1_inpt != random_num:
                    plyr_1_inpt = int(input('Wrong entry! Try again!'))
                    count += 1
    end_time = time.time()
    plyr_1_time = end_time - start_time
    print('It took Player 1', (plyr_1_time), 'seconds')
    return plyr_1_time
def player_2_times():
    any_key = input("Player 2 press any key when you're ready to begin")
    print('Player 2 type the number shown as quickly as possible')
    start_time = time.time()
    count = 0
    while count < 4:
        count += 1
        for i in range(0, 3):
            random_num = randint(0, 9)
            plyr_2_inpt = int(input(f'Type {random_num}: '))
            if plyr_2_inpt == random_num:
                count += 1
                continue
            else:
                while plyr_2_inpt != random_num:
                    plyr_2_inpt = int(input('Wrong entry! Try again!'))
                    count += 1
    end_time = time.time()
    plyr_2_time = end_time - start_time
    print('It took Player 2', (plyr_2_time), 'seconds')
    return plyr_2_time

p1_time = player_1_times()
p2_time = player_2_times()


if p1_time > p2_time:
    import turtle

    player1_turtle = turtle.Turtle()
    player2_turtle = turtle.Turtle()

    player1_turtle.color('red')
    player2_turtle.color('blue')

    player1_turtle.speed(2)
    player2_turtle.speed(2)
    input('Press any key to see the distance traveled in leg 1 of the race')
    player1_turtle.forward(50)
    player2_turtle.forward(25)
    input('Press any key to see the distance traveled in leg 2 of the race')
    player1_turtle.forward(50)
    player2_turtle.forward(25)
    input('Press any key to see the distance traveled in leg 3 of the race')
    player1_turtle.forward(50)
    player2_turtle.forward(25)
    turtle.exitonclick()
    print('Player 1 is the winner!')
elif p2_time > p1_time:
    import turtle

    player1_turtle = turtle.Turtle()
    player2_turtle = turtle.Turtle()
    
    player1_turtle.color('red')
    player2_turtle.color('blue')

    player1_turtle.speed(2)
    player2_turtle.speed(2)
    input('Press any key to see the distance traveled in leg 1 of the race')
    player1_turtle.forward(25)
    player2_turtle.forward(50)
    input('Press any key to see the distance traveled in leg 2 of the race')
    player1_turtle.forward(25)
    player2_turtle.forward(50)
    input('Press any key to see the distance traveled in leg 3 of the race')
    player1_turtle.forward(25)
    player2_turtle.forward(50)
    turtle.exitonclick()
    print('Player 2 is the winner!')