sales_data = [
('Marcus Webb', 'East', 4250.00),
('Priya Sharma', 'West', 5875.50),
('DeShawn Carter', 'East', 3100.75),
('LaTonya Rivers', 'South', 6420.00),
('Bob Nguyen', 'West', 4980.25),
]

top_performer_threshold = 5000

for name, region, total in sales_data:
    formatted_total = f"{total:,.2f}"
    print(f"{name}, {{region}}, ${formatted_total}")
    if total > top_performer_threshold:
        print(" ^ Top performer!")