import turtle
from random import randint

turtle.colormode(255) #set colormode to 255

tim = turtle.Turtle() #inistialise turtle obj

#set properties for tim
tim.shape('arrow')
tim.width(3)
tim.speed(0)

#number of circles
n = int(input("Enter number  of circles : "))

screen = turtle.Screen() #initialise screen object

for i in range(0,n):
    #pick random color for tim 
    rand_color = (randint(0,255), randint(0,255), randint(0,255))
    tim.color(rand_color)
    tim.circle(200) #draw circle
    tim.left(360 / n) #rotate


screen.exitonclick()