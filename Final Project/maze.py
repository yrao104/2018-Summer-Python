import turtle
import random

#MAZE CODE:

#makes a screen object and sets the background picture to a snowy image
screen = turtle.Screen()
pic = "snow.jpg"
screen.bgpic(pic)

#makes a list called blocks
blocks = []

#function called makeBlock that essentially makes a block in the maze at a certain point
def makeBlock(x, y, t):
  t.speed(0)
  screen = turtle.Screen()
  t.penup()
  #makes the turtle travel to a certain point before becoming an ice block
  t.goto(x, y)
  t.pendown()
  #set the turtle to an image that looks like an ice block
  image1 = "block (5).png"
  screen.addshape(image1)
  t.shape(image1)
  #makes the image upright
  t.right(90)
  #adds the turtle used to the blocks list
  blocks.append(t)

#code that makes the entire iceblock maze
#two simple variables to run the makeBlock function while making sure the blocks are placed in a pattern
#all the code below is pretty much the same
n = 1
x = 0
for i in range(1):
  for i in range(1):
    tn = turtle.Turtle()
    tn.speed(0)
    makeBlock(-185, 185, tn)#makes the block at a sepcific location with a certain turtle
    n+=1
    x+=1
  for i in range((185*2+33) // 33 - 1):
    tn = turtle.Turtle()
    tn.speed(0)
    makeBlock(-185, (185 - 33*x), tn)#the variables are used to assure that no block is made twice
    n+=1
    x+=1
  x = 1
  n = 1
  for i in range(185*2 // 30):
    tnt = turtle.Turtle()#a new turtle variable is created each time
    tnt.speed(0)
    makeBlock((-185 + 30*x), (185 - 33*11), tnt)
    n+=1
    x+=1
  x = 1
  n = 1
  for i in range(185*2 // 33):
    tntt = turtle.Turtle()#the turtle variables changes per loop to assure that they are different
    tntt.speed(0)
    makeBlock(-185+30*12, ((185 - 33*11) + 33*x), tntt)
    n+=1
    x+=1
  x = 1
  n = 1
  for i in range((185*2 - 30) // 30):
    tnttt = turtle.Turtle()
    tnttt.speed(0)
    #numbers are used to assure that the loop creates blocks ar precise location
    #based on the block image's length and width in pixels
    makeBlock(((-185+30*12) - 30*x), (185 - 33*11 + 33*11), tnttt)
    n+=1
    x+=1
  n = 1
  x = 1
  for i in range(4):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((-154 + 30*x), 120, ttnt)
    x+=1
    n+=1
  n+=1
  x = 1
  for i in range(4):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock(((-154 + 30*5) + 30*x), 120, ttnt)
    x+=1
    n+=1
  n+=1
  x = 1
  for i in range(3):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock(116, (120 - 33*x), ttnt)
    x+=1
    n+=1
  n+=1
  x = 1
  for i in range(3):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock(116, (-12 - 33*x), ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(5):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((116 - 30*x), -111, ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(3):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((-64 - 30*x), -111, ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(2):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((-124 + 30*(x - 1)), (-11+33*2), ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(5):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((-94 + 30*x), 25, ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(1):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock((56 - 30*2), (25 + 33*2), ttnt)
  n+=1
  x = 1
  for i in range(7):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock(((-4 + 30*3) - 30*x), (91 - 4*33), ttnt)
    n+=1
    x+=1
  n+=1
  x = 1
  for i in range(1):
    ttnt = turtle.Turtle()
    ttnt.speed(0)
    makeBlock(-124, (-41+33), ttnt)
