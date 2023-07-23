
# A list of items in the menu
menu = ["Coffee", "Tea", "Sandwich", "Cake"]

# Create a dictionary to store the stock values for each item
stock = {
    "Coffee": 10,
    "Tea": 15,
    "Sandwich": 5,
    "Cake": 8
}

# A dictionary to store the prices for each item
price = {
    "Coffee": 2.5,
    "Tea": 2.0,
    "Sandwich": 5.0,
    "Cake": 3.5
}

# Calculate the total stock worth in the cafe
total_stock_worth = 0

for item in menu:
    item_value = stock[item] * price[item]
    total_stock_worth += item_value

# Print the result
print("The total stock worth in the cafe is:", total_stock_worth)
