'''
Yamuna Rao
7/2
Ask the user for an integer. Print all of the even numbers between that number and 0. Then print all of the odd 
numbers between that number (inclusive) and 0.
'''

number = input("Enter a number:")
num = int(number)
if num % 2 == 1:
  print("These are all of the even numbers between " + number + " and 0.")
  for x in range(num-1, 1, -2):
    print x
  print("These are all of the odd numbers between " + number + " and 0.")
  for x in range(num, 1, -2):
    print x
if num % 2 == 0:
  print("These are all of the odd numbers between " + number + " and 0.")
  for x in range(num-1, 1, -2):
    print x
  print("These are all of the even numbers between " + number + " and 0.")
  for x in range(num, 1, -2):
    print x
