'''
Yamuna Rao
7/9
Choose minimum of two  functions and two events you are not familiar with.READ the description, Google , Experiment with the minimum 
functions. ( points)
You may include additional Turtle , Screen methods that you already know.
You MUST include comments in your code describing (in your own words) what the functions do and what you programmed (created))
Demonstrate your ability to use the functions, try to go beyond simple print statements , simple functionalities.
'''
import turtle

turtle.shape("turtle") 
# moves turtle to a certain point wihtout leaving a trail
turtle.penup()
turtle.goto(-100,0)
turtle.pendown()
#makes the turtle lightblue
turtle.color("lightblue")
turtle.forward(100)
#NEW FUNCTION #1
turtle.dot(100, "lightblue") #creates a lightblue dot(size in pixels, color)
turtle.forward(100)

#NEW FUNCTION #2
#fills turtle color w/ violet and black border
turtle.fillcolor("violet")

#turtle does function without leaving a trace(invisible)
def fun():
  turtle.penup()
  turtle.goto(100,100)
  turtle.pendown()
  turtle.dot(100, "lightgreen") #creates a lightgreen dot at the point (50, 50)
#NEW EVENT #1
turtle.onrelease(fun())

#when the user drags the turtle, it creates a drawing
#if the penup function is used, the user can drag the turtle anywhere leaving an invisible trail
turtle.penup()
#NEW EVENT #2
turtle.ondrag(turtle.goto)

#makes the turtle black and makes it write text with parameters
turtle.color("black")
turtle.write("Move the turtle inside the blue circle", move = True, align = "right", font=("Arial", 13, "normal"))

#creates a function where the turtle writes text with parameters
#makes the function run after 6000 milliseconds on a timer
def function():
  turtle.write("Good Job!   ", move = True, align = "right", font=("Arial", 13, "normal"))
screen = turtle.Screen()
screen.ontimer(function, 6000) # runs function fun after 360 milliseconds
