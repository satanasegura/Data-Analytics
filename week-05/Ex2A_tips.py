# Define known values
food_cost = 79.25
tax = 6.54
tip = 12.00
# Calculate the unknown
total_due = food_cost + tax + tip
# Display the results
print("The total due is " + str(total_due))
# the str is there because it is taking line 6 and the variables of what total_due is
# which is the value of food_cost, tax, and tip

# we will print the string food_cost which is 79.25 to "food cost is" and add
# "and tax is" to the string of tax which is 6.54

print("Food cost is " + str(food_cost) + " and tax is " + str(tax))
print("Tip is " + format(tip, ".2f"))
print("Total due is " + str(total_due))
