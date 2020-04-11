import turtle
import random

screen = turtle.Screen()
image = "token (3).png"

tokens = []#makes a list called tokens
score = 0#makes sure that the initail score is 0

# a function that generates a single token
def generateToken(x, y):
  t = turtle.Turtle()
  t.speed(0)
  t.isActive = True#uses a boolean value
  t.pu()
  t.left(90)
  screen.addshape(image)
  t.shape(image)
  t.goto(x, y)
  tokens.append(t)#adds the turtle used to the tokens list

# Generate 10 tokens at certain locations
#assures that the tokens don't appear on blocks in the maze where the character can't reach them
generateToken(-5, 152)
generateToken(145, 152)
generateToken(-155, 119)
generateToken(-35, 86)
generateToken(-95, 20)
generateToken(115, -13)
generateToken(-155, -79)
generateToken(-65, -145)
generateToken(-5, -79)
generateToken(145, -145)

  
#makes a scoreTurtle turle that writes the score in the bottom left hand corner of the screen  
scoreTurtle = turtle.Turtle()
scoreTurtle.ht()
scoreTurtle.pu()
scoreTurtle.goto(-170, -160)
scoreTurtle.write("Score: " + str(score), align = "left", font = ("Arial", 15))
  
# Function called by creature.py when the player touches a token
def touchedToken(token):
  # Hide and remove references to the token which was touched
  token.reset()
  token.ht()
  
  # Create property isActive to keep track of whether or not token should be used in collision detection
  token.isActive = False
  
  # Increase the score by 10
  global score # Tell python "score" should not be made local to the scope of this function
  score = score + 10
  
  # Rewrite the score
  scoreTurtle.clear()
  scoreTurtle.write("Score: " + str(score), align = "left", font = ("Arial", 15))



  
