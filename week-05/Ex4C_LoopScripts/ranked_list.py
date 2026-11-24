skills = ["Financial Analysis", "Data Analysis", "Statistics", "Python", "SQL", "Machine Learning"]

for index, skill in enumerate(skills, start = 1):
    if index == 1:
        print(f"{index}. {skill} <- top pick!")
    else:
        print(f"{index}. {skill}")
        
