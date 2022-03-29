#Sean Kelley
#Ch4 Lab 1
#25 June 2021

import math

print("Jane's Stuff Shop")
print()
total_cost = []
items_purchased = int(input("How many items would you like to purchase: "))
count = 1
for n in range(items_purchased):
    prices = float(input(f"Enter price of item {count}: "))
    total_cost.append(prices)
    count +=1
cost = float(format(sum(total_cost), '.2f'))
average_cost = format(cost / (count - 1), '.2f')
print()
print(f"Your total price is is :${cost}")
print(f"The average price of your items is ${average_cost}")