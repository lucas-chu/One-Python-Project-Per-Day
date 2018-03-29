import turtle
# Draw all normal polygons
# draw half a dozen patterns
# tessellate
# draw a geometric dragon
# draw a spiral, a log spiral
# draw a mandelbrot set
# draw half a dozen fractals
# draw a turtle and a dragon
'''
class Vector2D:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  def __add__(self, other):
    return Vector2D(self.x + other.x, self.y + other.y)
'''

def triangle():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(120)

def square():
  for _ in range(4):
      turtle.forward(50)
      turtle.left(90)

def squareflower():
  for _ in range(18):
      turtle.left(20)
      square()

def pattern():
    p = [20, 50, 10, 55, 55, 10, 50, 20]
    n = 0
    for _ in range(10):
        for _ in range(8):
            turtle.forward(n)
            turtle.left(90)
            n = n + 1

def draw_spiral(radius):
    #outward steady spiral
    original_xcor = turtle.xcor()
    original_ycor = turtle.ycor()
    speed = 1
    while True:
        turtle.forward(speed)
        turtle.left(10)
        speed += 0.1
        if turtle.distance(original_xcor, original_ycor) > radius:
            break

def hexagon():
  for _ in range(6):
      turtle.forward(100)
      turtle.left(60)

def hexa():
    for _ in range(6):
        turtle.right(120)
        triangle()
        turtle.forward(100)
        turtle.right(60)

def honeycomb():
    for _ in range(6):
        turtle.pos = (0.0, 0.0)
        hexagon()
        turtle.forward(100)
        turtle.right(60)


turtle.speed(10)
turtle.exitonclick()



