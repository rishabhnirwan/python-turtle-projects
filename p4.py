import turtle
from random import randint

colors = ['black', 'blue', 'blue4', 'green', 'DarkGreen', 'IndianRed4', 'pink', 'orange1', 'magenta4', 'red', 'red4']

tim = turtle.Turtle()
tim.shape('arrow')
tim.width(5)

def rand_move(dist):
    n = randint(0,3)
    match n:
        case 0:
            tim.forward(dist)
        case 1:
            tim.right(90)
            tim.forward(dist)
        case 2:
            tim.left(90)
            tim.forward(dist)
        case 3:
            tim.backward(dist)

screen = turtle.Screen()
screen.delay(5)


step = 0
d = 100
while step <= 100:
    rand_color =colors[randint(0, len(colors) - 1)] #random color 
    tim.color(rand_color)
    rand_move(d)
    step += 1

screen.exitonclick()