name = input("Please enter name: ")

# print("Hello " + name)

drink = input("What would you like to drink: ")
# print(drink)

whipped_cream = input("Do you want whipped cream (Yes/No): ")
# print(whipped_cream)
quantity = input("How many would you like: ")
# print(quantity)

# if whipped_cream == "yes":
#     print(quantity + " " + drink + " with wipped cream coming right up!")
# else:
#     print(quantity + " coffe coming right up!")

order = name, drink, whipped_cream, quantity,



print(f"Name: {name}, drink: {drink}, cream: {whipped_cream}, quantity: {quantity}.")

print(order)