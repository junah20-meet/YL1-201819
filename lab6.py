#1
from turtle import *
import random, math

class Ball(Turtle):
    def __init__(self, radius, color, speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1=Ball(5, "blue", 3)
ball2=Ball(6, "black", 6)

def check_collision(ball1, ball2):
    r1 = ball1.radius
    r2 = ball2.radius
    x1 = ball1.xcor()
    x2 = ball2.xcor()
    y1 = ball1.ycor()
    y2 = ball2.ycor()
    d = math.sqrt((x2-x1)**2+(y2-y2)**2)
    if r1+r2 <= d:
        print("colliding")
        
list1 = [ball1, ball2]
def 
