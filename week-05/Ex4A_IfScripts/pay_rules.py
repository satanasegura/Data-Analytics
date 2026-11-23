pay_rate = 12.50
hours_worked = 50

gross_pay = hours_worked * pay_rate

if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * pay_rate * .50
    gross_pay = gross_pay + overtime_pay

print(f"Gross pay: ${gross_pay: .2f}")