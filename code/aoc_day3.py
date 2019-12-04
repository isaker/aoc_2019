import sys

filepath = '../input/day3input.txt'

def execute_moves(m):
	coordinates_list = []
	x_coordinate = 0
	y_coordinate = 0
	coordinates_list.append((x_coordinate, y_coordinate))
	for move in moves:
		direction = move[0]
		distance = int(move[1:])
		print str.format("Moving {} steps in direction {}", distance, direction)
		if direction == 'R':
			for x in xrange(1,distance+1):
				x_coordinate += 1
				coordinates_list.append((x_coordinate, y_coordinate))
		elif direction == 'L':
			for x in xrange(1,distance+1):
				x_coordinate -= 1
				coordinates_list.append((x_coordinate, y_coordinate))
		elif direction == 'U':
			for y in xrange(1,distance+1):
				y_coordinate += 1
				coordinates_list.append((x_coordinate, y_coordinate))
		elif direction == 'D':
			for y in xrange(1,distance+1):
				y_coordinate -= 1
				coordinates_list.append((x_coordinate, y_coordinate))
	print str.format("History of coordinates: {}", coordinates_list)
	return coordinates_list

def execute_moves2(int, m):
	x_coordinate = 0
	y_coordinate = 0
	steps = 0
	print str(m)
	for move in moves:
		direction = move[0]
		d = move[1:]
		print d
		distance = d
		print str.format("Moving {} steps in direction {}", distance, direction)
		if direction == 'R':
			for x in xrange(1,distance+1):
				steps += 1
				x_coordinate += 1
				if int == (x_coordinate, y_coordinate):
					print "found intersection after " + str(steps) + " steps"
					break
		elif direction == 'L':
			for x in xrange(1,distance+1):
				steps += 1
				x_coordinate -= 1
				if int == (x_coordinate, y_coordinate):
					print "found intersection after " + str(steps) + " steps"
					break
		elif direction == 'U':
			for y in xrange(1,distance+1):
				steps+= 1
				y_coordinate += 1
				if int == (x_coordinate, y_coordinate):
					print "found intersection after " + str(steps) + " steps"
					break
		elif direction == 'D':
			for y in xrange(1,distance+1):
				steps+= 1
				y_coordinate -= 1
				if int == (x_coordinate, y_coordinate):
					print "found intersection after " + str(steps) + " steps"
					break
	return steps

def steps_to_intersection(ins):
	

	shortest_combined = 100000000000000000
	for i in ins:
		combined_steps = 0
		for line in lines:
			line = line.rstrip('\n')
			moves = line.split(',')
			combined_steps += execute_moves2(i, moves)
		if combined_steps < shortest_combined:
			shortest_combined = combined_steps
	return shortest_combined

with open(filepath) as f:
	lines = f.readlines()

inters = [(976, -940), (938, -940), (431, -1122), (192, -1122), (-20, -1275), (-20, -1691), (-48, -1831), (-273, -1691), (-491, -1583), (-574, -1277), (-574, -1177), (-129, -1149), (192, -1149), (431, -434), (287, 1680), (321, 1553), (321, 1411), (0, 1411), (-30, 1411), (-91, 1680), (266, 1680), (0, 1310), (-30, 1310), (-204, 1310), (-211, 1310), (-570, 1309), (-898, 1313), (-817, 1592), (-780, 1592), (-745, 1592), (-745, 1691), (-780, 1691), (-817, 1691), (-1176, 1544), (-1397, 1313), (-632, 1087), (-632, 1309), (-632, 1521), (-632, 1699), (-644, 1923), (-780, 1923), (-817, 1923), (-899, 1903), (-817, 1888), (-811, 1903), (-811, 1969), (-811, 2353), (-644, 2354), (-26, 3264), (-26, 3317), (29, 3317), (29, 3264), (6, 3264), (6, 3317)]
print steps_to_intersection(inters)



		

#with open(filepath) as f:
#	lines = f.readlines()

#histories = []

#for line in lines:
#	line = line.rstrip('\n')
#	moves = line.split(',')
#	print str(moves)
#	histories.append(execute_moves(moves))

#hist1 = histories[0]
#hist2 = histories[1]
#intersections = []

#print "hist1 length = " + str(len(hist1))
#print "hist2 length = " + str(len(hist2))
#total = len(hist1) * len(hist2)
#count = 0 
#for c1 in hist1:
#	for c2 in hist2:
#		count += 1
#		sys.stdout.write("progress: %d/%d   \r" % (count, total) )
#		sys.stdout.flush()
#		if c1 == c2:
#			intersections.append(c1)

#print str(intersections)
#intersections = intersections[1:]
#print str(intersections)

#shortest_dist = 100000000
#closest = ()
#for ints in intersections:
#	dist = abs(ints[0]) + abs(ints[1])
#	if dist < shortest_dist:
#		shortest_dist = dist
#		closest = ints

#print "closest: " + str(closest)
#print "distance: " + str(shortest_dist)
