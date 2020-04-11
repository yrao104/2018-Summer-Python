
'''
Yamuna Rao
6/28
Ask the user to enter 3 unique integers and determine the min , mid and max of the 3 numbers
'''
num1 = input("Enter an integer:")
num2 = input("Enter a different integer:")
num3 = input("Enter a different integer")

a = int(num1)
b = int(num2)
c = int(num3)

if a < b and a < c and b < c:
  print("min: " + str(a))
  print("mid: " + str(b))
  print("max: " + str(c))
elif a < b and a < c and c < b:
  print("min: " + str(a))
  print("mid: " + str(c))
  print("max: " + str(b))
elif b < c and b < a and c < a:
  print("min: " + str(b))
  print("mid: " + str(c))
  print("max: " + str(a))
elif b < c and b < a and a < c:
  print("min: " + str(b))
  print("mid: " + str(a))
  print("max: " + str(c))
elif c < b and c < a and a < b:
  print("min: " + str(c))
  print("mid: " + str(a))
  print("max: " + str(b))
elif c < b and c < a and b < a:
  print("min: " + str(c))
  print("mid: " + str(b))
  print("max: " + str(a))
