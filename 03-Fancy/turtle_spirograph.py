# Draw a colorful spirograph using turtle graphics
import turtle
import colorsys

t = turtle.Turtle()
t.speed(0)
turtle.bgcolor("black")

# Create a list of RGB colors from HSV spectrum
colors = [colorsys.hsv_to_rgb(i/36, 1, 1) for i in range(36)]

for i in range(360):
    color = colors[i % 36]
    t.pencolor(color)
    t.circle(100)
    t.right(10)

turtle.done()