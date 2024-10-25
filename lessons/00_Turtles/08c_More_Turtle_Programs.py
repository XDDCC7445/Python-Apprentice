"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Background Image"


Then change the code so that the turtle has a different image ( look in the 'images'
  ) and moves to the corners of the screen in a square pattern. 
"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

t = turtle.Turtle()                  # Create a turtle named tina

def set_background_image(window, image_name):
    

    from pathlib import Path
    from PIL import Image


    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    image = Image.open(image_path)
    
    window.setup(image.width, image.height, startx=0, starty=0)
    window.bgpic(image_path)

screen = turtle.Screen()
screen.setup(width=600, height=600)

   
set_background_image(screen, "moustache1.gif") 



def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)




set_turtle_image(t, "pikachu.gif")

t.penup()
t.speed(5)
for i in range(100):
    t.goto(300,300)
    t.goto(300,-300)
    t.goto(-300,-300)
    t.goto(-300,300)



turtle.exitonclick()      

