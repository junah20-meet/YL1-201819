import turtle
 
myTurtle = turtle.Turtle(shape="turtle")
myTurtle.pencolor('green')
myTurtle.circle(50)
                  
myTurtle.pencolor('yellow')
myTurtle.penup()
myTurtle.setposition(-120, 0)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor('red') 
myTurtle.penup()
myTurtle.setposition(60,60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor('black') 
myTurtle.penup()
myTurtle.setposition(-60, 60)
myTurtle.pendown()
myTurtle.circle(50)

myTurtle.pencolor('blue') 
myTurtle.penup()
myTurtle.setposition(-180, 60)
myTurtle.pendown()
myTurtle.circle(50)
 
turtle.mainloop()

