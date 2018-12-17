#1
import turtle

for i in range(5):
    turtle.fd(150)
    turtle.right(144)

#2
import turtle

turtle.begin_fill()
turtle.fd(40)
turtle.right(90)
turtle.fd(30)
turtle.right(45)
turtle.fd(30)
turtle.right(90)
turtle.fd(30)

turtle.right(45)
turtle.fd(30)
turtle.end_fill()

#3
from turtle import *
screen = Screen()
#screen.register_shape("wallpaper.gif")
#turtle.shape("wallpaper.gif")

#4
import turtle
turtle.speed(0)
for i in range(500):
    turtle.fd(200)
    turtle.right(45)
    turtle.fd(100)
    turtle.right(90)
    turtle.fd(50)
    turtle.home()
    turtle.right(i)
