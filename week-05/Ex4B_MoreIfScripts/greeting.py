hour = int(input("Enter the hour (0-23): "))

if hour >= 23 or hour <= 4:
    greeting = "What are you doing up so late??"
elif hour < 10:
    greeting = "Good morning!"
elif hour < 17:
    greeting = "Good day!"
else:
    greeting = "Good evening!"  
print(greeting)