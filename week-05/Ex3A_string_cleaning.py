name_1 = "PRIYA SHARMA"
name_2 = "bob NGUYEN"
name_3 = "LaTonya Williams"
salary_1 = "$82,500"
salary_2 = "$74,000"

print(name_1.lower())
print(name_2.lower())
print(name_3.lower())

print(name_1.title())
print(name_2.title())
print(name_3.title())

sal1_clean = salary_1.replace("$", "")
sal2_clean = salary_2.replace("$", "")
print(sal1_clean) 
print(sal2_clean)
print(type(sal1_clean))

result = int(salary_1.replace("$", "").replace(",", ""))
print(result)
print(type(result))
