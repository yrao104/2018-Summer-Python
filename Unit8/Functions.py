import turtle

def pentagon():
  turtle.color("teal")
  turtle.begin_fill()
  for i in range(5):
    turtle.forward(50)
    turtle.left(72)
  turtle.end_fill()
  
#pentagon()#invokes function and runs it

def returnSomething():
  print("something")
  #return 5 #when this line of code is commented out, the console returns None
#creats a function that prints something and returns the number 5

'''
def absolute_value(num): #num is a local variable since it can only be used in the function
  """This function returns the absolute #docstring
  value of the entered number""" #this is called a  docstring
  
  if num>=0:
    return num
  else:
    return -num
absolute_value()
'''
#scope, global, local (variables)

def my_func():
  global x #makes x a global variable
  x = 10
  print("Value inside function:",x)
#scope
x = 20 # this x is a gloabl variable(can be accessed anywhere)
print(x)
my_func()
print("Value outside function:",x) #prints 10 since the x in the function is global

