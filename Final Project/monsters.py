import turtle
import random
import math

from creature import turtle as playerTurtle

screen = turtle.Screen()
image = "monster (1) (1).png"


# For collision detection to work in this context because of the synchronous nature of python the
# monsters must move in small increments and check for collisions in-between. Rather than rewrite
# paths I have made the monster's movement random. 


monsters = [] #creates a list called monsters

#function that creates a monster using an image and random integers
def createMonster():
  t = turtle.Turtle()
  t.pu()
  t.speed(0)
  t.goto(0, 60)
  screen.addshape(image)
  t.shape(image)
  monsters.append(t)
  # Make the turtle face a random direction but not directly at (0, 0)
  t.left(random.randint(-120, 120))

#a function that moves the monster and makes sure it is traveling a random path
#makes sure monster is moving throughout the game
def moveMonsters():
  for monster in monsters:
    monster.speed(0)
    monster.forward(10)
    monster.right(random.randint(-50, 50))
    
    # Turn the monster arround if they are going off screen
    if monster.xcor() > 200 or monster.xcor() < -200 or monster.ycor() > 200 or monster.ycor() < -200:
      monster.left(180)
      monster.forward(20)
    
    # Check for collisions with the player
    if monster.distance(playerTurtle.xcor(), playerTurtle.ycor()) < 15:
      textTurtle = turtle.Turtle()
      textTurtle.pu()
      textTurtle.color("red")
      textTurtle.ht()
      textTurtle.goto(0, -20)
      textTurtle.write("Game Over", align = "center", font = ("Arial", 25,"bold"))
      exit()
    
  # Ask screen to call this function again in a tenth of a second
  screen.ontimer(moveMonsters, 0.1)
  
moveMonsters()

# Create five initial monsters  
for i in range(5):
  createMonster()
