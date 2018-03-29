import turtle
import random

def ngon(x):
    n = 360/x
    for x in range(x):
        turtle.forward(10)
        turtle.left(n)

def log(x):
    # where x = the base

    turtle.forward()


# phi = (1 + 5 ** (1 / 2)) / 2
# print(phi)
# input

print( 'Numbers of sides: ' , end = ' ' )
x = int(input())

# turtle stuff
turtle.speed(10)

while True:
    ngon(x)
    if turtle.pos == (0,0):
        turtle.done()




