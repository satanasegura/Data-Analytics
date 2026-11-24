student_name = "Noah" 
student_major = "MKT"

major_name = ""
department_office = ""

if student_major == "BIOL":
    major_name = "Biology"
    department_office = "Science Bldg, Room 310"
elif student_major == "CSI":
    major_name = "Computer Science"
    department_office = "Sheppard Hall, Room 314"
elif student_major == "ENG":
    major_name = "English"
    department_office = "Kerr Hall, Room 201"
elif student_major == "HIST":
    major_name = "History"
    department_office = "Kerr Hall, 114"
elif student_major == "MKT":
    major_name = "Marketing"
    department_office = "Westly Hall, Room 310"
else:
    major_name = "Unknown Major"
    department_office = "Unknown Office"

print("Student Name:", student_name)
print("Major:", major_name)
print("Department Office:", department_office)