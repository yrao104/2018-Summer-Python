import commentedTurtleGame#when running this code puta # before the import polygon
import polygon #When runing the polygon code put # before the import commentedTurtleGame
'''
import turtle
import math
'''
#in object oriented program, there are intances, constructors, and methods
'''
#2 turtle objects. tina and tim
tina = turtle.Turtle() #Turtle() is a constructor that lives in the turtle class(it constructs objects)
tim = turtle.Turtle()

tina.color("red")
tim.color("teal")

#1 turtle forward and 1 turtle back
tina.forward(100)
tim.back(100)

#makes background color lavender
screen = turtle.Screen()
screen.bgcolor("lavender")

#the classes above have already been defined in the python library
'''
'''
#define a class (class names should be capitalized)

class Circle:
  def __init__(self, r): #constructor(construct an object for the class)
    self.radius = r #instance variable, makes every variable have a radius of 1
    #the inital data for the circle(above)
    #self means that it is associated with the object
    
  def getRadius(self): #accessor or getter methods
    return self.radius
    
  def setRadius(self, r): #mutator methods or setter methods
    self.radius = r
    
  def area(self): #utility methods
    return self.radius * self.radius * math.pi
    
  def drawCircle(self, t):
    t.circle(self.radius)

t1 = turtle.Turtle()
#create a circle object, call it what you want
circle = Circle(50)
#draw circle
circle.drawCircle(t1)
#print the radius of that circle
print(circle.getRadius()) #use an accessor method to get instance variable
'''

import math
import turtle

class Circle:
  def __init__(self, r): #constructor(construct an object for the class)
    self.radius = r #instance variable, makes every variable have a radius of 1
    #the inital data for the circle(above)
    #self means that it is associated with the object
    
  def getRadius(self): #accessor or getter methods
    return self.radius
    
  def setRadius(self, r): #mutator methods or setter methods
    self.radius = r
    
  def area(self): #utility methods
    return self.radius * self.radius * math.pi
    
  def drawCircle(self, t):
    t.circle(self.radius)

circle1 = Circle()#finds the class and calls the constructor
t1 = turtle.Turtle()#makes another object(turtle)
circle1.drawCircle(t1)#utility method

circle2 = Circle()
#change circle2 radius to 100
circle2.setRadius(100) #calls setRadius function and changes function
#drawCircle
circle2.drawCircle(t1)
