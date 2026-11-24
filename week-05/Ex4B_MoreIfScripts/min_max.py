a = 365
b = 2942
c = 2139

smallest = a
if b < smallest:
    smallest = b
if c < smallest:
    smallest = c    

largest = a
if b > largest:
    largest = b
if c > largest:
    largest = c

print("Smallest:", smallest)
print("Largest:", largest)