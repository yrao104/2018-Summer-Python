'''
Yamuna Rao
7/16
Study the following code and comment 80 percent of it
'''

# Adapted from “Python Programming Fundamentals” by Kent Lee
# http://knuth.luther.edu/~leekent/IntroToComputing/

from turtle import * #lets functions run from the turtle library without having to write turtle before the function in the code
import random
import math

screen = Screen()


screenMinX = -screen.window_width()/2 #makes a variable that equals the negative value of the width of half the screen
screenMinY = -screen.window_height()/2 #makes a variable that equals the negative calue of height of half the screen
screenMaxX = screen.window_width()/2 #makes a variable that equals half the width of the screen
screenMaxY = screen.window_height()/2#makes a variable that equals half the height of the screen

screen.setworldcoordinates(screenMinX,screenMinY,screenMaxX,screenMaxY)#sets the screen to a certain length and width
#4 values are required to set the screen(2 x-values and 2 y-values)
screen.bgcolor("black")

penup()
ht()#hides the turtle (ht stands for hideturtle) #I used a stack oveflow to decipher this
speed(0)
goto(0, screenMaxY - 20)
color('grey')
write("Turtles in Space!!", align="center", font=("Arial",20))
goto(0, screenMaxY - 33)
write("Use the arrow keys to move and 'x' to fire", align="center")
goto(0, 0)
color("red")


class Bullet(Turtle): #creates a class called Bullet where Turtle is the parameter
  def __init__(self,screen,x,y,heading):#constructor
    Turtle.__init__(self)#initializes the turtle
    self.speed(0)
    self.penup()
    self.goto(x,y)
    self.seth(heading)#sets the heading to heading
    self.screen = screen 
    self.color('yellow')
    self.max_distance = 500#makes the maximum distance traveled 500 pixels
    self.distance = 0#initializes the distance to 0
    self.delta = 20#sets the initial time duration to 20 seconds # I had to search this up as I was confused by this line
    self.shape("bullet")#makes the shape a bullet
  
  def move(self):#creates a function for the Bullet called move
    self.distance = self.distance + self.delta #makes the distance equal the distance traveled plus the number of seconds
    self.forward(self.delta)#moves forward 20 pixels
    if self.done():#if the function is completed, reset
      self.reset()
      
  def getRadius(self):#accessor function
    return 4
    
  def blowUp(self):#creats a function called blowUp
    self.goto(-300,0)
  
  def done(self):#creates a function called done
    return self.distance >= self.max_distance #returns that the ditance traveled is greater than or equal to the maximum distance

class Asteroid(Turtle): #ctreates another class called Asteroid
  def __init__(self,screen,dx,dy,x,y,size):
    Turtle.__init__(self)#initializes turtle
    self.speed(0)
    self.penup()
    self.goto(x,y)
    self.color('lightgrey')
    self.size = size
    self.screen = screen
    self.dx = dx#sets the sine of the turtle's heading to dx (I got these to lines from http://ccl.northwestern.edu/netlogo/2.1/docs/dictionary.html)
    self.dy = dy#sets the cosine of the turtle's heading to dy
    self.shape("rock" + str(size))
    
  def getSize(self):#creates an accessor called getSize
    return self.size#returns the size of the screen
  
  def getDX(self):#creates an accessor called getDX
    return self.dx#returns the sine of the turtle's heading
  
  def getDY(self):#creates an accessor that returns the cosine of the turtle's heading
    return self.dy
  
  def setDX(self,dx):#function that sets the dx to the Aseteroid class's dx
    self.dx = dx
      
  def setDY(self,dy):# sets the dy to the Asteroid's dy
    self.dy = dy
      
  def move(self):#creates a function called move
    x = self.xcor()#sets x and y to the Asteroid's coordinates
    y = self.ycor()

    x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX #makes sure that the Asteroid does not exceed any boundaries using modules and the min and max values of the screen
    y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
    
    self.goto(x,y)#makes the Asteroid goto the certain point
    
  def blowUp(self):#creates a function called blowUp
    self.goto(-300,0)

  def getRadius(self):#creates a getter function that returns the size of the asteroid times 10 minus 5
    return self.size * 10 - 5

class SpaceShip(Turtle):#creates a class called Spaceship that has the turtle as its parameter
  def __init__(self,screen,dx,dy,x,y):
    Turtle.__init__(self)#initializes the turtle
    self.speed(0)
    self.penup()
    self.color("white")
    self.goto(x,y)
    self.dx = dx#sets the sine of the turtle's heading to dx (I got these to lines from http://ccl.northwestern.edu/netlogo/2.1/docs/dictionary.html)
    self.dy = dy#sets the cosine of the turtle's heading to dy
    self.screen = screen   
    self.bullets = []#creates a list called self.bullets
    self.shape("turtle")

  def move(self):#creates a function that moves the Spaceship based on teh boundaries of the screen size(as was done above for the Asteroid class)
    x = self.xcor()
    y = self.ycor()

    x = (self.dx + x - screenMinX) % (screenMaxX - screenMinX) + screenMinX
    y = (self.dy + y - screenMinY) % (screenMaxY - screenMinY) + screenMinY
    
    self.goto(x,y)
  
  def powPow(self, asteroids):#creates a function powPow that has the asteroids as its parameter
    dasBullets = []#list
    for bullet in self.bullets:#for loop that moves the bullet 
      bullet.move()
      hit = False#if the bullet hits something, it holds a boolean value of false
      for asteroid in asteroids:#for loop for assteroids
        if intersect(asteroid, bullet):#if statement for if the asteroid and bullet hit each other
          asteroids.remove(asteroid)#removes asteroid
          asteroid.blowUp()#makes asteroid run blow up function
          bullet.blowUp()#makes bullet run blow up function
          hit = True#if asteroid and bullet intersect, hold boolean value of true
      if (not bullet.done() and not hit):#if the bullets were not hit, this adds the bullet back to the list dasBullets
        dasBullets.append(bullet)
          
             
    self.bullets = dasBullets #makes one list equal to another
  
  def fireBullet(self):#creates a function called fireBullet 
    self.bullets.append(Bullet(self.screen, self.xcor(), self.ycor(), self.heading()))
    #adds the different parameters from the bullet function to a list
    
  def fireEngine(self):#creates a function called fireEngine
    angle = self.heading()#sets a variable angle as the heading
    x = math.cos(math.radians(angle))#makes x equal to the radians of angle times cosine
    y = math.sin(math.radians(angle))#makes y equal to the radians of angle times sine
    self.dx = self.dx + x#adds the value of the self.dx and self.dy from before to x and y
    self.dy = self.dy + y
  
  def turnTowards(self,x,y):#creates a function called turnTowards 
    if x < self.xcor():#if statement that if x is less than the actual x-coordinate, move left 7 pixels
      self.left(7)
    if x > self.xcor():#if x is less than the actual x-coordinate, move right 7 pixels
      self.right(7)
   
  def getRadius(self):#creates a getter function called getRadius
      return 10#returns the radius, 10
  
  def getDX(self):#getter funcion
      return self.dx
  
  def getDY(self):#getter function
      return self.dy

def intersect(object1,object2):#function called intersect with two parameters
  dist = math.sqrt((object1.xcor() - object2.xcor())**2 + (object1.ycor() - object2.ycor())**2)
  #calculates the distance between object 1 and object 2 using the distance formula between two points
  
  radius1 = object1.getRadius()#makes radius1 equal the radius of object1 using the getter function, getRadius
  radius2 = object2.getRadius()#makes radius2 equal the radius of object2 using the getter function, getRadius
  
  # The following if statement could be written as 
  # return dist <= radius1+radius2
  if dist <= radius1+radius2:#if statment for if the distance is less than the sum of both radiuses
      return True#return the boolean value True
  else:
      return False#if note, False

screen.register_shape("rock3",((-20, -16),(-21, 0), (-20,18),(0,27),(17,15),(25,0),(16,-15),(0,-21)))
#makes rock3 shapes on the screen in 8 different places using coordinates
screen.register_shape("rock2",((-15, -10),(-16, 0), (-13,12),(0,19),(12,10),(20,0),(12,-10),(0,-13)))
#makes rock2 shapes on the screen in 8 different places using sepcific coordinates
screen.register_shape("rock1",((-10,-5),(-12,0),(-8,8),(0,13),(8,6),(14,0),(12,0),(8,-6),(0,-7)))
#makes rock1 shapes on the screen in 9 places
screen.register_shape("ship",((-10,-10),(0,-5),(10,-10),(0,10)))
#makes ship shapes on the screen in 4 places
screen.register_shape("bullet",((-2,-4),(-2,4),(2,4),(2,-4)))
#makes bullet shapes on the screen in 4 places

ship = SpaceShip(screen,0,0,(screenMaxX-screenMinX)/2+screenMinX,(screenMaxY-screenMinY)/2 + screenMinY)
#makes ship equal toa value, using the SpaceShip function and different parameters

asteroids = []#list

for k in range(5):
  dx = random.random() * 6 - 3#random.random() generates a random number
  dy = random.random() * 6 - 3
  x = random.random() * (screenMaxX - screenMinX) + screenMinX
  y = random.random() * (screenMaxY - screenMinY) + screenMinY

  asteroid = Asteroid(screen,dx,dy,x,y,random.randint(1,3))
  #makes asteroid equal to a value using the function Asteroid from above with parameters

  asteroids.append(asteroid)#adds asteroid to the asteroid lis ton line 203

def play():
  # Tell all the elements of the game to move
  ship.move()
  
  gameover = False#lets the game continue
  for asteroid in asteroids:
    asteroid.move()#moves asteroid
    if intersect(ship,asteroid):#if asteroid intersects with ship
      write("BOOM!!!",font=("Arial",30),align="center")#writes messagage across screen
      #lets user know that the ship and asteroid hit
      gameover = True#makes the game over
  
  ship.powPow(asteroids)#uses powPow function from above
  
  screen.update()#makes the screen go back to its usual state
  
  if not asteroids:#if there are no asteroids
    color('green')#words in green
    write("You Win!",font=("Arial",30),align="center")#lets user know that they won

  #if the game is not over, lets the game run for 30 more seconds
  if not gameover:
    screen.ontimer(play, 30)

bullets = []#list

def turnLeft():#function turnLeft for the ship to turn left 7 degrees
  ship.left(7)

def turnRight():#functin turnRight for ship to turn right 7 degrees
  ship.right(7)

def go():#function that makes ship fire engine
  ship.fireEngine()

def fire(): #function taht makes the ship fire a bullet        
  ship.fireBullet()

ht()#hides the turtle

screen.tracer(0);#turns turtle animation off and lets drawing update (I used https://docs.python.org/2/library/turtle.html as my source to find this information)

#simple functions to make the turtle move right, left, up and fire
screen.onkey(turnLeft, 'left')
screen.onkey(turnRight, 'right')
screen.onkey(go, 'up')
screen.onkey(fire, 'x')
screen.listen()#makes the screen listen to the user and onkey functions

play()#I am not really sure what this means (does it play a sound or make some action happen on the screen?)
