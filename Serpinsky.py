
from turtle import *
turt = Turtle()
turt.penup()
turt.goto(-300, -300)
turt.pendown()
def sierpinski(t, i, s,):
   if (i == 0):
       t.seth(0)
       t.begin_fill()
       for i in range(3):
           t.speed("fastest")
           t.fd(s)
           t.lt(120)
       t.end_fill()
   else:
       for angle in [0, 120, -120]:
           t.speed("fastest")
           sierpinski(t, i - 1, s)
           t.lt(angle)
           t.fd(s * 2 ** (i - 1))
       t.seth(0)
sierpinski(turt, 10, 5)