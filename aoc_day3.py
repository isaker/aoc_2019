filepath = 'day3input.txt'

def execute_moves(m):
	x_coordinate = 0 
	y_coordinate = 0 
	for move in moves:
		direction = move[0]
		distance = move[1:]
		print str.format("Moving {} steps in direction {}", distance, direction)
		

with open(filepath) as f:
	lines = f.readlines()

for line in lines:
	line = line.rstrip('\n')
	moves = line.split(',')
	print str(moves)
	execute_moves(moves)