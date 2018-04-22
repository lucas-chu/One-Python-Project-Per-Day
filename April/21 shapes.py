import turtle
loadWindow = turtle.Screen()
turtle.speed(100)
# Draw all normal polygons
# draw half a dozen patterns
# tessellate
# draw a geometric dragon
# draw a spiral, a log spiral
# draw a mandelbrot set
# draw half a dozen fractals
# draw a turtle and a dragon
# def sin():

size = 5
sides = 6

def shape(size, sides):
    for i in range(sides):
        turtle.forward(size)
        turtle.left(360/sides)

def hourglass():
    turtle.circle(5 * i)
    turtle.circle(-5 * i)

for i in range(50):
    shape(3*i, sides)
    turtle.left(i)

turtle.exitonclick()