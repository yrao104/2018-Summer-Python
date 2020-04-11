'''
Yamuna Rao
7/10
create one large lab  or 3 medium labs that includes events: (key binding, click, 
timer,ondrag, onrelease etc.) see Trinket Python libraries and readings for a list 
of events) MUST include comments
'''
import turtle
import time

#makes the background color of the screen dark red(the color of lava)
screen = turtle.Screen()
screen.bgcolor("darkred")

#makes the turtle speed 0 to make it move faster
turtle.speed(0)

#hides the turtle(makes it invisible) and makes the turtle go to a certain point and make a grey dot
turtle.hideturtle()
turtle.penup()
turtle.goto(-150, 50)
turtle.pendown()
turtle.dot(50, "grey")

#makes more gray dots without leaving a trail in an overlapping patter
turtle.penup()#makes sure the dot is invisible
turtle.goto(150, 50)#makes the turtle go to a certain point before making the dot
turtle.pendown()
turtle.dot(50, "grey")#makes a grey dot, 50 pixels wide
turtle.penup()
turtle.goto(170, 50)
turtle.pendown()
turtle.dot(50, "grey")
turtle.penup()
turtle.goto(190, 50)
turtle.pendown()
turtle.dot(50, "grey")
turtle.penup()
turtle.goto(210, 50)
turtle.pendown()
turtle.dot(50, "grey")
turtle.penup()
turtle.goto(230, 50)
turtle.pendown()
turtle.dot(50, "grey")

#makes a teal turtle called bob in the shape of a turtle
#bob then goes to a certain point without leaving a trail
bob = turtle.Turtle()
bob.color("teal")
bob.shape("turtle")
bob.penup()
bob.goto(-150, 50)
bob.pendown

#creates a turtle callsd words and makes the turtle invisisble
words = turtle.Turtle()
words.hideturtle()

#makes words write sentences and makes the previous sentences go away
words.write("Bob the turtle is stranded on a sinking rock surrounded by lava.", None, "center", ("arial", 10))
time.sleep(5) # giving the user 3 seconds to read each sentence
words.clear() # erases the previous sentence
words.write("Save Bob by clicking in between the two rocks to create a bridge.", None, "center", ("arial", 10))
time.sleep(5)
words.clear()
words.write("Then, drag Bob across the bridge to the exit on the other side.", None, "center", ("arial", 10))
time.sleep(5)
words.clear()
words.write("Hurry up! You have 1 minute", None, "center", ("arial", 10, "bold"))
time.sleep(5)
words.clear()

#creates a function where a long, grey rectangle is created
def makebridge(x, y):
  turtle.penup()# the turtle leaves no trail
  turtle.setpos(x, y)#sets the turtle's position to wherever the user clicks
  turtle.pendown()
  turtle.color("darkgrey")
  turtle.begin_fill()#fills in the rectangle
  #makes a rectangle
  turtle.right(90)
  turtle.forward(15)
  turtle.left(90)
  turtle.forward(300)
  turtle.left(90)
  turtle.forward(30)
  turtle.left(90)
  turtle.forward(300)
  turtle.left(90)
  turtle.forward(15)
  turtle.end_fill()
  
screen.onclick(makebridge)#performs the function above when the user clicks the button

bob.penup()#makes sure bob leaves no trail 
bob.ondrag(bob.goto)#lets the user drag bob anywhere on the screen

#creates a turtle called scribe and makes the turtle invisible
scribe = turtle.Turtle()
scribe.hideturtle()

#creates a function where bob's x-coordinate is used to see if the user has moved bob after 1000 milliseconds
#if the user moved bob, the turtle(scribe) writes that bob was saved
def quick():
  xcor = bob.xcor()#creates a variable equal to the decimal value of bob's x-coordinate
  if xcor != -150.0:
    scribe.write("Great job! You saved Bob!", None, "center", ("arial", 20))
screen.ontimer(quick, 1000)
  
#creates a function where bob's x- coordinate is used to see if the user has moved bob after a full minute
#if the user has moved bob, the turtle(scribe) writes that bob is saved
#if the user has not moved bob, turtle(scribe) writes that time is up
def bobalive():
  xcor = bob.xcor()#creates a variable equal to the decimal value of bob's x-coordinate(-150)
  if xcor == -150.0:
    scribe.write("Oh no, time is up!", None, "center", ("arial", 20))
  else:
    scribe.write("Great job! You saved Bob!", None, "center", ("arial", 20))
screen.ontimer(bobalive, 60000)
