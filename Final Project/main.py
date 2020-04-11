'''
Yamuna Rao
7/19
Final Project
'''
# I imported the rest of the tabs of code at the bottom in a screen.onclick function
#I did that to make sure that the other code did not clash with the code for my introduction to the game

import turtle

screen = turtle.Screen()
#screen object for adding images

#Code for the INTRO to explain the game:

scribe = turtle.Turtle()
#creates a turtle called scribe
scribe.hideturtle()
#makes the turtle invisible, hides it

pic = "snow.jpg"
# makes a variable equal the link of an image
screen.bgpic(pic)
#makes the background picture the image above

#makes variable equal the links for images
pic1 = "character (1) (1) (2).png"
pic2 = "token (3).png"
pic3 = "monster (1) (1).png"

#adds the shapes for the three pictures above to the turtle's screen
screen.addshape(pic1)
screen.addshape(pic2)
screen.addshape(pic3)

#makes 4 turtle objects that will be used later in the program
t = turtle.Turtle()
turtle1 = turtle.Turtle()
turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()

#THE WRITING IN THE INTRO:
t.hideturtle() #hides the turtle
t.penup() #makes the turtle leave no trace when moving
t.color("darkblue") #makes the turtle dark blue
t.goto(-195, 160) #makes the turtle move to a certain location
t.write("Welcome to the Ice Challenge!", None, align = "top", font = ("arial", 20, "bold"))
#makes the turtle write a sentence with certain other parameters like font, size, and alignment

#repeats the steps above in the lines below to write more sentences on the screen
#explains the game to the user so they know how to play
t.goto(0, 100)
t.write("Move the blue character            through the", None, "center", ("arial", 13))

#makes a picture of the blue character go to the space in between character and through as shown above
#there is a space above to insert the picture of the character so that the player understands better
turtle1.shape(pic1) #makes the turtle's shape an image
turtle1.speed(0)
turtle1.penup()
turtle1.left(90)
turtle1.goto(50, 110)

#more writing as part of the intro
t.goto(0, 60)
t.write("ice maze using the arrow keys. Collect all", None, "center", ("arial", 13))
t.goto(0, 20)
t.write("the fruits            along the way and stay", None, "center", ("arial", 13))

#another picture corresponding the the fruits so the character knows what they look like
turtle2.shape(pic2)
turtle2.speed(0)
turtle2.penup()
turtle2.left(90)
turtle2.goto(-55, 30)

#more writing as part of the intro
t.goto(0, -20)
t.write("away from the monsters            !", None, "center", ("arial", 13))

#another picture corresponding the the monsters so the character knows what they look like
turtle3.shape(pic3)
turtle3.speed(0)
turtle3.penup()
turtle3.left(90)
turtle3.goto(90, -10)

#more writing as part of the intro
t.goto(0, -60)
t.write("Click 'Start Game' on the bottom", None, "center", ("arial", 13))
t.goto(0, -100)
t.write("to begin.", None, "center", ("arial", 13))

#creates a "button" that the user can press to go to the actual game
button = turtle.Turtle() #makes a turtle called button
button.hideturtle() #hides the turtle
button.color("darkblue") #makes the turtle dark blue
button.penup()
button.goto(140, -150)
button.write("Start", align = "center", font = ("arial", 10)) #writes words on the screen
button.goto(140, -165)
button.write("Game", align = "center", font = ("arial", 10))

#imports the rest of the code after the introduction
#so that the words don't clash with the images for the game
def importRestofCode(x, y): 
  #since I had to use screen.onclick, I had to use x and y as the two parameters for my function
  
  #clears the words and images in the intro
  t.clear()
  turtle1.hideturtle()
  turtle2.hideturtle()
  turtle3.hideturtle()
  
  #makes the button go away and 
  button.clear()
  
  #a quick chunk of code to use the x and y parameters that does not do anything on the screen
  invisible = turtle.Turtle()
  invisible.hideturtle()
  invisible.penup()
  invisible.goto(x, y)
  
  #imports the other tabs
  import othermaze
  import creature
  import monsters
  import tokens

#uses screen.onclick so that after the button in the intro is pressed, the other code is imported
#after the code is imported, the user can play the game
#assures that the intro and game don't clash
screen.onclick(importRestofCode)
