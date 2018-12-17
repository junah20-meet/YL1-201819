#1
from turtle import *
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
