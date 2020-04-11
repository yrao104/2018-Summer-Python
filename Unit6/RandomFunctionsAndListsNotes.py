import customlab
import randomintegers
import randomnumbers
import randomColorCircles
import randomcolorz
import random
import turtle

'''
#prints 20 random numbers from 18 - 35 (not including 36)
for i in range(20):
  numb = random.randrange(18, 36)
  print(numb)
  #instead of the two lines above, you can say: print(random.randrange(18, 36)
'''

'''
#prints 20 random numbers from 1 - 10 (including 1 and 10)
for i in range(50):
  numb = random.randint(1,10)
  print(numb)
'''

'''
#prints random even numbers between 1-20
for i in range(20):
  numb = random.randint(1, 20)
  if (numb % 2 == 0):
    print(numb)
'''   
'''
LISTS
Lists are a collection of values. Elements are the values in a list.
'''

'''

myList = [1, 2, 3, 4]
#index/subscript of the elements in the list above : 0,1,2,3
# -1 is the last element (4), -2 is the second to last element (3)
# if you want to print 3 you would say print(myList[2])
emptyList = []
stuff = [1, 2, 3, 4, "I delcare a thumb war"]
print(myList)

print("The length of my list is " + str(len(myList)))
# len is a function that prints the length of a list
print(myList[3] + myList[2])  # prints 7 : 4+3
print(stuff[4])

#lists can store other lists
numbers = [1, 2, 3, 4]
stringsList = ["I", "kicked", "my", "toe"]
myList = [numbers, stringsList]
print(myList)

friendsList = ["Ananya", "Varsha", "Avishi", "Ayeeshi", "Mira", "Priyanka"]
#change 4th element, then print list
friendsList[3] = "another person"
print(friendsList)

friendsList.append("something at the end")
#adds somthing to the end of the list

print(friendsList)

del(friendsList[3])
#deletes 4th element in the list

print(friendsList)

friendsList.insert(3, "Satyam")
#inserts string after the 4th element in the list

print(friendsList)
'''

'''
#turtleobject, named Alex
screen  = turtle.Screen ()
screen.bgcolor("black")
alex = turtle.Turtle()
for aColor in ["yellow", "red", "purple", "blue"]:
  #code that makes a random pen size 
  size = random.randint(1, 100)
  alex.pensize(size)
  #using the variable isn't neccessary
  alex.color(aColor)
  alex.forward(100)
  alex.left(90)
'''
'''
colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"] # a list of colors
turtle.width(10) # makes the width of the line 10 pixels
length = 50

for count in range(100):
  color = random.choice(colors) # chooses a random color from the colorslist
  turtle.forward(length)
  turtle.right(135)
  turtle.color(color)
  length = length + 5
'''
