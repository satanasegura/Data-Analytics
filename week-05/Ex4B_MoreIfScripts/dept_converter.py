dept_code = int(input("Enter a department code: "))

if dept_code == 1:
    dept_name = "Marketing"
elif dept_code == 5: 
    dept_name = "Human Resources"
elif dept_code == 10:
    dept_name = "Accounting"
elif dept_code == 12:
    dept_name = "Legal"
elif dept_code == 18:
    dept_name = "IT"
elif dept_code == 20:
    dept_name = "Customer Relations"
else: 
    dept_name = "Unknown department"
print(dept_name)
