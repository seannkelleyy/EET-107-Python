#Sean Kelley  Chapter 2 Lab 1 16 June 2021

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
marbles_purchased = input("How many marbles would you like to purchase: ")
print()
marble_price = 1.27
print("Order prepared for " + first_name + " " + last_name)
print()
print(marbles_purchased + " marbles purchased @ $",marble_price)
print()
total_cost = float(marbles_purchased) * float(marble_price)
print("Total cost is $",total_cost)