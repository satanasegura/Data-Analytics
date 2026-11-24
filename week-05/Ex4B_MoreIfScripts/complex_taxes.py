hours = float(input("Enter the number of hours worked in a week: "))
pay_rate = float(input("Enter the hourly pay rate: "))
filing_status = input("Enter filing status ('single' or 'joint'): ").strip().lower()

weekly_gross_pay = hours * pay_rate
annual_gross_pay = weekly_gross_pay * 52

tax_rate = 0.0

if filing_status == "single":
    if annual_gross_pay < 12000:
        tax_rate = 0.05
    elif annual_gross_pay < 25000:
        tax_rate = 0.10
    elif annual_gross_pay < 75000:
        tax_rate = 0.15
    else:
        tax_rate = 0.20
elif filing_status == "joint":
    if annual_gross_pay < 12000:
        tax_rate = 0.0
    elif annual_gross_pay < 25000:
        tax_rate = 0.06
    elif annual_gross_pay < 75000:
        tax_rate = 0.11
    else:
        tax_rate = 0.20

weekly_tax_withheld = weekly_gross_pay * tax_rate
weekly_net_pay = weekly_gross_pay - weekly_tax_withheld

print("You worked", hours, "hours this period.")
print("Because you earn $" + str(pay_rate) + "per hour, your gross weekly pay is $" + str(weekly_gross_pay))
print("Your filing status is", filing_status)
print("Your tax withholding for the week is $" + str(weekly_tax_withheld))
print("Your net pay is $" + str(weekly_net_pay))
