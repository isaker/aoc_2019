filepath = 'day1input.txt'

def fuel_needed(mass):
	fuel = (mass / 3) - 2 
	if fuel < 0:
		return 0
	return fuel + fuel_needed(fuel)

with open(filepath) as f:
    lines = f.readlines()

tot_fuel = 0
for line in lines:
	mass = int(line)
	fuel_cost = fuel_needed(mass)
	tot_fuel += fuel_cost
print tot_fuel