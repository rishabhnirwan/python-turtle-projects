import turtle
from random import randint

colors = ['black', 'blue', 'blue4', 'green', 'DarkGreen', 'IndianRed4', 'pink', 'orange1', 'magenta4', 'red', 'red4']

tim = turtle.Turtle()
tim.shape("arrow")
tim.teleport(-100,300)

screen = turtle.Screen() #screen object initialized
screen.delay(15)


n = 3 # number of sides in the polygon

while n <11:
    theta = 360 / n # angle at 'corners' of the polygon
    rand_color =colors[randint(0, len(colors) - 1)] #random color 
    tim.color(f"{rand_color}")
    for i in range(0,n):
        #repeat n times for n sides
        tim.forward(200)
        tim.right(theta)
    n += 1 


screen.exitonclick()