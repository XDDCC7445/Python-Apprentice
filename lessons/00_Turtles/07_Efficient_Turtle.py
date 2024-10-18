
""""
More Efficient Turtles

Use what you've learned about functions and variables to make a program that
can draw a square, pentagon, and hexagon with a single function
"""


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window

tina = turtle.Turtle()                  # Create a turtle named tina

tina.shape('turtle')                    # Set the shape of the turtle to a turtle
tina.speed(2)                           # Make the turtle move as fast, but not too fast. 

    
for i in range(4):
    print ('loop iteration', i)
    
    tina.forward(100)                       
    tina.left(90)
tina.penup()                         
tina.goto(100,100)
tina.pendown()
for i in range(5):
    print ('loop iteration', i)
    
    tina.forward(100)                       
    tina.left(72)
tina.penup()
tina.goto(-100,100)
tina.pendown()
sides = 6
angle = 360/sides
for i in range(6):
    print ('loop iteration', i)
    
    tina.forward(100)                       
    tina.left(angle)


turtle.exitonclick()                     # Close the window when we click on it
