# Connect 4ys, 4x, x,	y. x+1,y+1, ... 
import turtle

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