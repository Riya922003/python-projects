from turtle import *

bgcolor('black')  # Set the background color to black
speed(0)          # Set the drawing speed to the maximum
hideturtle()      # Hide the turtle

# Draw a series of circles with rotation and color change
for i in range(100):  # Change the range for more circles
    color('red')      # Set the color to red
    circle(i)         # Draw a circle with increasing radius
    color('orange')   # Change color to orange
    circle(i * 0.5)   # Draw a smaller circle within
    right(3)          # Rotate the turtle slightly
    forward(3)        # Move the turtle forward slightly

done()  # Keep the window open
