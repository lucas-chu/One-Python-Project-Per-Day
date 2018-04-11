import turtle
# Draw all normal polygons
# draw half a dozen patterns
# tessellate
# draw a geometric dragon
# draw a spiral, a log spiral
# draw a mandelbrot set
# draw half a dozen fractals
# draw a turtle and a dragon



def chessboard():
    for _ in range(8):
        for _ in range(8):
            for _ in range(5):
                turtle.forward(50)
                turtle.left(90)
            turtle.right(90)
        turtle.left(90)
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(400)
        turtle.left(180)


turtle.speed(100)
chessboard()
turtle.exitonclick()



