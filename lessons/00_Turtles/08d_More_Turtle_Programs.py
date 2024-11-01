"""
Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section " Click on the Turtle"

Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and when you click on it, it moves to a random location on the screen.
"""



import random
x = random.randint(-300, 300)
y = random.randint(-300, 300)



# Double click on this cell to copy the code

import turtle as turtle

turtle.setup(width=600, height=600)

t = turtle.Turtle()

t.shape("turtle")
t.turtlesize(stretch_wid=10, stretch_len=10, outline=4) # Make the turtle really big

def turtle_clicked(t, x, y):
    t.goto(x,y)
    
    


t.onclick(lambda x, y, t=t: turtle_clicked(t, x, y))






turtle.done() 