import ChangeTendered
import JarChange
import Timelab
import ThreeMultidigit
import Conversion
import Arithmetic

'''
Yamuna Rao
6/21
Lecture2
'''


'''
print(5 + 5.0)
print(9 - 11)
print(4 * 3.14159265)

#/, //
print(6/3)
print(6//3)

#%
print(6 % 2)
print(2 % 6)
print(3 % 6)
print(1 % 6)
print(0 % 6)

print(2 ** 4)
#prints 2 to the power of 4
print(34 ** 34)
print(int(59.8))
#chops off decimal and prints 59
print(float(59))
#print 59.0, since floats have decimals

#ask a user to enter a number, numb1, ask for another number, numb2,
#score the sum in a variable called sum
# print "The sum of numb1 + numb2 = sum"

numb1 = input("Enter a number")
numb2 = input("Enter another number")
sum = (int(numb1) + int(numb2))
print("The sum of " + numb1 + " + " + numb2 + " = " + str(sum))

num1 = input("Enter a number with a decimal:")
num2 = input("Enter another number with a decimal")
product = int(float(num1)) * int(float(num2))
print("Your numbers are " + num1 + " and " + num2 + ". Their product is " + str(product))
'''

'''
EXPRESSIONS - combo of calues, variables, operators, and calls
to functions that need to be evaluated

MATH OPERATORS
+: addition
-: subtraction
*: multiplication
**: exponentian
/, //: division (/ produces numbers in decimals [float] (EX: 2.0)), // 
produces numbers in integers [int](EX: 2))
%: modules (remainder) (if the first number is less than the
second number, the answer to the modules is the first number)

*8.0 + 6 is 14.0, not 14
*print(float(6//5)) prints 1.0, not 1.2
