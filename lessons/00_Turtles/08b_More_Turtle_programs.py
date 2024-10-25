"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

"""
import turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)


t = turtle.Turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()
t.speed(5)

for i in range(100):
    t.goto(200, 200)
    t.goto(-200, -200)
    t.goto(200,-200)
    t.goto(-200,200)


turtle.exitonclick()     
