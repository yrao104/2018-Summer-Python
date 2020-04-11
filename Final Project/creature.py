import turtle

# Import the blocks list from the maze file for collision detection
from othermaze import blocks
from tokens import tokens, touchedToken
from tokens import score as SCORE

#makes sure that the player/creature does not leave a trail
turtle.penup()
#makes the creature travel fast
turtle.speed(0)
#makes sure the creature is upright on the screen
turtle.left(90)

#screen object
screen = turtle.Screen()

#stores the image in a variable
image = "character (1) (1) (2).png"

#add shape first and set the turtle shape
screen.addshape(image)
turtle.shape(image)

# The function that actually moves the turtle
def attemptMove(dX, dY):
  # Collision detection: Loop through each block and see if moving in the desired direction would cause a collsion
  for block in blocks:
    if block.distance(turtle.xcor() + dX, turtle.ycor() + dY) < 12:
      return
  turtle.goto(turtle.xcor() + dX, turtle.ycor() + dY)
  # Check for collisions with tokens
  for token in tokens:
    if token.isActive == True and token.distance(turtle.xcor(), turtle.ycor()) < 12:
      touchedToken(token)
  
# Call the attempt move with different delta x and delta y values based on what key is pressed
screen.onkey(lambda: attemptMove(0, 10), "Up")
screen.onkey(lambda: attemptMove(0, -10), "Down")
screen.onkey(lambda: attemptMove(-10, 0), "Left")
screen.onkey(lambda: attemptMove(10, 0), "Right")

screen.listen()

#a function to make sure that if the player collects all the tokens, "You Won!" is written on the screen
def checkifWon():
  for token in tokens:
    if SCORE == 100:
      writer.hideturtle()
      writer.penup()
      writer.goto(0, -20)
      writer = turtle.Turtle()
      writer.color("red")
      writer.write("You Won!", align = "center", font = ("Arial", 25,"bold"))
      exit()
  screen.ontimer(checkifWon, 0.1)#makes sure that the function is run after every 0.1 seconds

checkifWon()#runs the function
