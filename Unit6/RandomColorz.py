'''
Yamuna Rao
7/5
produce 3 random numbers ranging from 0 - 255 and set color of turtle
#Note instead of having literal integers like 255,
#you can assign variables
'''
import random
import turtle

for i in range(1):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
turtle.color(r, g, b)
turtle.pensize(5)
turtle.shape("turtle")
  
