'''
Yamuna Rao
7/15
Find the mean and median of any list by creating a function
'''
import copy


def meanmedian(a): #a is the name of the list 
  n = len(a) - 1
  num = 0
  while n >= 0:
    num = num + a[n]
    n = n - 1
  mean = num / len(a)
  order = []
  min = a[0]
  b = list(a)
  #c = list(a)
  '''
  for i in range(len(a)):
    for i in range(len(a)):
      if min >= a[i]:
        min = a[i]
    order.append(a[i])
    a.remove(a[i])
  '''
  a.sort()
  print(a)
  if len(a) % 2 == 1:
    median = a[len(a) // 2 + 1]
  else:
    median = (a[len(a) // 2 - 1] + a[len(a) // 2]) / 2
  print("The mean of the numbers is " + str(mean) + ".")
  print("The median of the numbers is " + str(median) + ".")
meanmedian([7, 9, 10, 3, 25, 6])

'''
def meanmedian(a): #a is the name of the list 
  n = len(a) - 1
  num = 0
  while n >= 0:
    num = num + a[n]
    n = n - 1
  mean = num / len(a)
  order = []
  min = a[0]
  b = a[:]
  for i in range(len(b)):
    for i in range(len(b)):
      if min > b[i]:
        min = b[i]
    order.append(b[i])
    b.remove(b[i])
  print(order)
  if len(order) % 2 == 1:
    median = order[len(order) // 2 + 1]
  else:
    median = (order[len(order) // 2 - 1] + order[len(order) // 2]) / 2
  print("The mean of the numbers is " + str(mean) + ".")
  print("The median of the numbers is " + str(median) + ".")
meanmedian([7, 9, 10, 3, 25, 6])
'''
    
 
