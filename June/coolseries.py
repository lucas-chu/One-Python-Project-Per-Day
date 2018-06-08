#cool series
import turtle 
import time
def triangle(length):
	for i in range(0,3):
		turtle.forward(length)
		turtle.left(120)


def sierpinski(length,depth):
	for j in range(0,3):
		if depth==1:
			triangle(length)
		else:
			sierpinski(length/2,depth-1)
	turtle.forward(length*2)
	turtle.left(120)

turtle.tracer(0,0)
sierpinski(400,4)
turtle.exitonclick()