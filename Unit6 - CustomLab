'''
Yamuna Rao
7/8
Combine turtle, lists, and random (all three items) to create a unique program or drawing. 
'''
import random
import turtle
screen  = turtle.Screen ()
screen.bgcolor("black")
xcor = random.randint(-20, 20)
ycor = random.randint(-20, 20)
turtle.speed(0)
turtle.penup()
turtle.goto(xcor, ycor)
turtle.pendown()
length = 5
for i in range(300):
  for i in range(3):
    colorList = [ "#e6fff7", "#ccffee", "#b3ffe6", "#99ffdd", "#80ffd4", "#66ffcc", "#4dffc3", "#33ffbb", "#1affb2", "#00ffaa", "#00e699", "#00cc88", "#00b377", "#009966", "#008055", "#006644"]
    color = random.choice(colorList)
    turtle.color(color)
    turtle.forward(length)
    turtle.right(120)
    length+=0.5
  turtle.right(2)
