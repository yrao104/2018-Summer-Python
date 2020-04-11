'''
Yamuna Rao
7/12
Create a function, listEven that receives a list, and returns a list of all even numbers in the
list, test your function
'''

def listEven(a): #a is the list name
  evensList = []
  for i in range(len(a)):
    if a[i] % 2 == 0:
      evensList.append(a[i])
  print(evensList)
listEven([7, 9, 10, 3, 25, 6]) #runs function
