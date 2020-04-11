'''
Yamuna Rao
6/22
Write an application that determines the value of coins inputted by user and prints the total in 
dollars and cents. It should ask the user the number of coins for each coin type 
(pennies, nickels, etc.)
'''

quarters = input("Enter the number of quarters:")
dimes = input("Enter the number of dimes:")
nickels = input("Enter the number of nickels:")
pennies = input("Enter the number of pennies:")
a = int(quarters) * 25 + int(dimes) * 10 + int(nickels) * 5 + int(pennies)
c = a // 100
d = a - c * 100
print("Total value: " + str(c) + " dollars and " + str(d) + " cents.")
