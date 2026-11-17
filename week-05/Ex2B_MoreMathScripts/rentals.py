import math

X = 38

seats_per_van = 15
cost_per_van = 250

num_vans = math.ceil(X / seats_per_van)
total_cost = num_vans * cost_per_van

cost_per_person = total_cost / X

print(f"Number of tourists (X): {X}")
print(f"Number of vans needed: {num_vans}")
print(f"Total cost: ${total_cost}")
print(f"Cost per person: ${cost_per_person}")   

# A: 19.74 per person
# B: 19.74 * 38 = 750
# C: 750 / 250 = 3 vans
# D: no money 