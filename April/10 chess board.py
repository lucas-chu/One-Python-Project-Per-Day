import turtle
# Draw all normal polygons
# draw half a dozen patterns
# tessellate
# draw a geometric dragon
# draw a spiral, a log spiral
# draw a mandelbrot set
# draw half a dozen fractals
# draw a turtle and a dragon



def square(x):
    for _ in range(x):
        for _ in range(5):
            turtle.forward(50)
            turtle.left(90)
        turtle.right(90)
    turtle.left(100)
    
turtle.speed(10)
square(8)
turtle.exitonclick()



