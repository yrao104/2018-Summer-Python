'''
Yamuna Rao
7/12
Create a function that receives 3 parameters (receives a turtle, side length and numbSides and draws
the polygon that results from the data received from the parameters:
def drawPolygon(t, sideLength, numSides):
# your code here.
wn = turtle.Screen()
geo = turtle.Turtle()
drawPolygon(geo,30,10) # draw a decagon , NOTE: function should be able to draw different polygons
'''
import turtle

def drawPolygon(t, sidelength, numsides):#t and bob are the same turtle
  for i in range(numsides):
    turtle.forward(sidelength)
    turtle.left(360 / numsides)


bob = turtle.Turtle()
drawPolygon(bob, 75, 7)#runs the function with the parameters
