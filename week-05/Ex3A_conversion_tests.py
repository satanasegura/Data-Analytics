# Description: This script tests various numeric
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

a_converted = float(a)
b_converted = int(b)
c_converted = int(c.split()[0])
d_converted = int(d.split()[-1])

print(a_converted)  
print(b_converted)  
print(c_converted) 
print(d_converted)  

print(float(a))
print(int(b))

print(int(float(a)))

print(int(c[0:3]))

print(a.strip())
print(d.strip())