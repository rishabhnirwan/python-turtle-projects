import turtle

tim_the_turtle = turtle.Turtle() #Create turtle object
tim_the_turtle.teleport(100,100) #teleport to (100,100) position
tim_the_turtle.shape("arrow")    #Set shape as arrow
tim_the_turtle.color("black")    #Set Color as black





screen = turtle.Screen() #Create the screen



for i in {1,2,3}:
    #Turn right and move forward, repeat this 4 times for square
    tim_the_turtle.right(90)
    tim_the_turtle.forward(200)

tim_the_turtle.right(90)
tim_the_turtle.forward(190)

screen.exitonclick()