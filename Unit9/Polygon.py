'''
Yamuna Rao
7/16
Create a class that makes an polygon with constructors, attributes, accessors, utility methods, mutator methods
'''
import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

colors = ["teal", "lavender", "gold", "red", "pink", "lightgreen", "lightblue", "aqua", "lightyellow"]

class Rectangle:
  def __init__(self, l, w):
    self.length = 1
    self.width = w
  
  def getLength(self):
    return self.length
  
  def getWidth(self):
    return self.width
  
  def setPosition(self, a, b):
    x = a
    y = b
  
  def setColor(self, a):
    color = "a"
  
  def setPensize(self, b):
    size = b
  
  def area(self):
    return self.width*self.length
  
  def drawRectangle(self, t, l, w):
    self.length = l
    self.width = w
    size = random.randint(1, 10)
    t.speed(0)
    t.pensize(size)
    color = random.choice(colors)
    t.color(color)
    t.begin_fill()
    t.forward(self.length)
    t.right(90)
    t.forward(self.width)
    t.right(90)
    t.forward(self.length)
    t.right(90)
    t.forward(self.width)
    t.end_fill()
shape = Rectangle(50, 25)
t = turtle.Turtle()
shape.drawRectangle(t, 50, 25)
