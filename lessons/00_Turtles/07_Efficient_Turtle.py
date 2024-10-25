"""
single function
"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=800, height=600)    # Set the size of the window
tina = turtle.Turtle()      




    

    


sides=4
angle=360/sides


for i in range(4):
    print ('loop iteration', i)
    tina.forward(100)                       
    tina.left(angle)

    
turtle.exitonclick()        