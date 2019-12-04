start = 284639
end = 748759

def valid(number):
	last_number = number[0]
	double_digits = False 
	never_decreases = True
	for n in number[1:]:
		if n == last_number:
			double_digits = True
		if int(n) < int(last_number):
			never_decreases = False
		last_number = n

	return double_digits and never_decreases

count = 0
for x in xrange(start,end + 1):
	if valid(str(x)):
		count += 1

print "4A | valid inputs: " + str(count)