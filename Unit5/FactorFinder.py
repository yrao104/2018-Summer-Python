'''
Yamuna Rao
7/2
Ask user for an integer. Then, using a loop, print all of the number’s factors.
'''

number = input("Enter a number:")
print("The factors are:")
num = int(number)
for x in range(1, num+1):
  if num % x == 0:
    print (x)
    
