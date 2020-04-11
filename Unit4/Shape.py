'''
Yamuna Rao
6/28
Let the user choose from 3 different shapes/polygons: example, 1. hexagon, 2. octagon, 3. pentagon , 
use if , elif and else , user enters a number then the corresponding shape is drawn,
'''
import turtle

polygon = input("Enter a number for a shape to be drawn (1 is a triangle, 2 is an octagon, and 3 is a decagon): )")
if polygon == "1":
  turtle.right(60)
  turtle.forward(100)
  turtle.right(120)
  turtle.forward(100)
  turtle.right(120)
  turtle.forward(100)
elif polygon == "2":
  turtle.penup()
  turtle.goto(5, 100)
  turtle.pendown()
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
  turtle.forward(100)
  turtle.right(45)
else:
  turtle.penup()
  turtle.goto(5, 100)
  turtle.pendown()
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  turtle.forward(70)
  turtle.right(36)
  
