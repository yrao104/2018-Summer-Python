'''
Yamuna Rao 
6/28
Create a custom if else lab- example text game, customizing turtles, moving left or right etc or choose one of the labs shown
in Google Drive
'''
import turtle
polygon = input("Enter the name of a polygon  in lowercase letters that you want to be drawn (The polygon must have 3-10 sides):")

if polygon == "triangle" or polygon == " triangle":
  turtle.right(60)
  turtle.forward(100)
  turtle.right(120)
  turtle.forward(100)
  turtle.right(120)
  turtle.forward(100)
elif polygon == "square" or polygon == " square":
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(100)
elif polygon == "rectangle" or polygon == " rectangle":
  turtle.forward(150)
  turtle.right(90)
  turtle.forward(100)
  turtle.right(90)
  turtle.forward(150)
  turtle.right(90)
  turtle.forward(100)
elif polygon == "pentagon" or polygon == " pentagon":
  turtle.right(108)
  turtle.forward(100)
  turtle.right(72)
  turtle.forward(100)
  turtle.right(72)
  turtle.forward(100)
  turtle.right(72)
  turtle.forward(100)
  turtle.right(72)
  turtle.forward(100)
elif polygon == "hexagon" or polygon == " hexagon":
  turtle.penup()
  turtle.goto(5, 100)
  turtle.pendown()
  turtle.forward(100)
  turtle.right(60)
  turtle.forward(100)
  turtle.right(60)
  turtle.forward(100)
  turtle.right(60)
  turtle.forward(100)
  turtle.right(60)
  turtle.forward(100)
  turtle.right(60)
  turtle.forward(100)
  turtle.right(60)
elif polygon == "heptagon"or polygon == " heptagon":
  turtle.penup()
  turtle.goto(50, 0)
  turtle.pendown()
  turtle.right(180 - (360/7))
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  turtle.right(360/7)
  turtle.forward(100)
  '''
  turtle.right(360/7)
  turtle.right(100)
  turtle.right(360/7)
  turtle.right(100)
  turtle.right(360/7)
  turtle.right(100)
  turtle.right(360/7)
  turtle.right(100)
  turtle.right(360/7)
  turtle.right(100)
  turtle.right(360/7)
  turtle.right(100)
  '''
elif polygon == "octagon" or polygon == " octagon":
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
elif polygon == "nonagon" or polygon == " nonagon":
  turtle.right(140)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
  turtle.right(40)
  turtle.forward(50)
elif polygon == "decagon" or polygon == " decagon":
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
