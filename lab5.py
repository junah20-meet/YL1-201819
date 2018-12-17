#1
import turtle
from turtle import turtle
import random

class Square(Turtle):
    def __init__(self, size, color):
        Turtle.__init__(self)
        self.shape("square")
        self.size=size
        self.color(color)

    def random(self):
        self.color(random.choice(['black' , 'blue']))

s1 = Square(5, 'black')

#2
class Hexagon(Turtle):
    def __init__(self, size):
        self.size=size
        Turtle.__init__(self)
        turtle.home()
        turtle.begin_poly()
        turtle.penup()
        turtle.left(90)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)
        turtle.fd(self.size)
        turtle.right(60)

        turtle.end_poly()
        p =turtle.get_poly()
        turtle.register_shape("Hexagon" , p)

hex = Hexagon(100)
turtle.mainloop()
