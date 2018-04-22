import turtle
import math
pi = math.pi

def triangle(a,b,c):
	# law of cosines, where ac = angle c
	ac = math.acos((a**2 + b**2 - c**2)/(2*a*b))*180/pi
	# law of sines
	ab = math.asin(math.sin(ac)/c*b)*180/pi
	# Angle sum theorem
	aa = ab + ac
	turtle.forward(a)
	turtle.left(180-ac)
	turtle.forward(b)
	turtle.left(180-ab)
	turtle.forward(c)
	turtle.left(aa)
turtle.setx(0)
turtle.sety(0)
triangle(30,40,50)
triangle(30,40,50)
turtle.exitonclick()