'''
Yamuna Rao
6/25
Directions: Write an application that reads the purchase price and the amount paid. Display the change in dollars, quarters, 
dimes, nickels, and pennies. The input value has to be in decimal value (exclude the dollar sign). You are not allowed to use
if statements or loops! Note: You may be off a penny, just sig fig issue.
'''

price = input("Enter the purchase price of an item (Exclude the dollar sign):")
given = input("Enter the money that you paid the cashier (Exclude the dollar sign): ")
print("The purchase price was $" + str(price))
print("You paid $" + str(given))
change = float(given) - float(price)
print("You recieved $" + str(change) + " as change.")
dollar100 = change// 100
dollar50 = change%100 // 50
dollar20 = change%100%50 // 20
dollar10 = change%100%50%20 // 10
dollar5 = change%100%50%20%10 // 5
dollar1 = change%100%50%20%10%5 // 1
quarters = change%100%50%20%10%5%1*100 // 25
dimes = change%100%50%20%10%5%1*100%25 // 10
nickels = change%100%50%20%10%5%1*100%25%10 // 5
pennies = change%100%50%20%10%5%1*100%25%10%5 // 1
print(str(int(dollar100)) + " one hundred dollar bill(s)")
print(str(int(dollar50)) + " fifty dollar bill(s)")
print(str(int(dollar20)) + " twenty dollar bills")
print(str(int(dollar10)) + " ten dollar bill(s)")
print(str(int(dollar5)) + " five dollar bill(s)")
print(str(int(dollar1)) + " one dollar bill(s)")
print(str(int(quarters)) + " quarters")
print(str(int(dimes)) + " dimes")
print(str(int(nickels)) + " nickels")
print(str(int(pennies)) + " pennies")
