'''
Yamuna Rao
6/28
Ask user to enter a number. Determine if the number is odd or even
'''
num = input("Enter a number:")
a = int(num)%2
if a == 0:
  print("Your number is even.")
elif a == 1:
  print("Your number is odd.")
