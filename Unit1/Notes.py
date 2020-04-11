import lab3
#import lab2
#import lab1
#import miniLab1

#import debugging1
#runs debugging1 before running main

'''
Yamuna Rao
6/18/18
Lecture Notes
'''

'''
import turtle
#is a statement that runs the function
'''

'''
Multi-line comments are used with a pair of 3 apostrophies
before and after the comment
'''

'''
#Single-line comments are used with the pound sign

turtle.color("red")
#makes the color of the turtle red
turtle.forward(100)
#makes the turtle move forward 100 units
'''

'''
For homework/labs the name, date, and description of the code
must be listed on the top (as shown above)

Also, additional comments should be used for methods and 
organizations
'''

'''
DATA TYPES
There are different data types in order to hold different kinds
of characters.
int -integer, (-3,-2,-1,0,1,2,3)
float - any number with decimals
boolean - true or false statements 
String - anything inside single or double parentheses
'''

'''
print(type(17))
#prints the datatype of the number/value
'''

'''
VARIABLES
A variable is a name that refers to a value. (identifier)
They contain letters, underscores, and numbers
They can't begin with numbers and can't have spaces.
They are case sensitive. (theName is a different variable
than thename)
You initialize variables through the assignment statement:
variableName = value
Ex: the data type is not needed in front of the variable
name
name = "Bob"
num = 3
'''

'''
PRINT
You can print strings and variables uwing the print function.
You use the plus sign (+) to combine string and bariables into
one printed statement.
They will be printed in the console
Ex:
num1 = 5
num2 = 7
bane = "Sally"
print("Learning is fun")
print(num1)
print(num1 + num2) #adds num1 and num2 together
print("My number is" +str(num1)) #str casts to string in order to print
#you must change number data types to string when printing strings and numbers
'''
'''
num1 = 5
num2 = 7

print("The answer is " + str(num1 + num2))
'''

'''
INPUT
You can take input from the user through the console and store it in a
variable.
You do this by using the input function.
This is important, as the code interacts with the user in many programs.
'''

'''
#Ex
enteredName = input("What is your name?")
#The code will wait for the user's input before continuing
print ("Hello" + enteredName)
'''

'''
#Exercise #6
enteredName = input("What is your name?") 
enteredAge = input("How old are you")
print ("Hello, " + enteredName + ". " + enteredAge + " years old is the best age!")
'''
'''
numb3 = input("enter numb3")
numb4 = input("enter numb4")
print(int(numb3) + int(numb4))
'''
