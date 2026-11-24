bank_balance = 10000
savings_goal = 1000
weekly_savings = 100
treat_cost = 25

halfway_goal = savings_goal * 0.5
three_quarter_goal = savings_goal * 0.75

while bank_balance < savings_goal:
    bank_balance = bank_balance + weekly_savings

    if bank_balance >= three_quarter_goal:
        bank_balance = bank_balance - treat_cost   
        print(f"So close! After treating myself, my balance is up to {bank_balance}.")
    elif bank_balance > halfway_goal:
        print(f"Almost there! This week my balance is up to {bank_balance}.")
    else:
        print(f"This week my balance increased to {bank_balance}.")
print(f"Goal met! My current balance is {bank_balance}.")

