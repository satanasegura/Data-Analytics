savings = 123000
interest_rate = 0.07
years = 72 / (interest_rate * 100)

print("Your current savings is $" + format(savings, ",.2f") + ".")
print("At a " + format(interest_rate, ".1%") + " interest rate, your savings account will be")
print("worth $" + format(savings * 2, ",.2f") + " in " + format(years, ".1f") + "years")
                         