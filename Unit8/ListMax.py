'''
Yamuna Rao
7/12
Create a function that receives a list in its parameters and loops the list to determine the
Largest (max) number. Please don’t use built in max function.
'''

def list(a):# a is the list name
  max = a[1]
  for i in range(len(a)):
    if max < a[i]:
      max = a[i]
  print(str(max) + " is the largest number.")
list([7, 9, 10, 3, 25, 6]) # runs the function
