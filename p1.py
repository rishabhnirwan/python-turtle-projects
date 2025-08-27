import turtle

tim = turtle.Turtle()
tim.shape("arrow")
tim.color("black")
tim.teleport(-300,0)

screen = turtle.Screen()

for i in range(0,4):
    tim.forward(75)
    v = tim.pos()
    x = v[0]
    tim.teleport(x+50, 0)


screen.exitonclick()