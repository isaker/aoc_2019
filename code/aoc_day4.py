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

def valid4b(number):
	last_number = number[0]
	double_digits = False
	never_decreases = True
	for x in xrange(1,len(number)):
		# print str.format("x = {}", x)
		# print str.format("using number {}", number[x])
		if number[x] == last_number:
			# print str.format("number[x] {} == last_number {}", number[x], last_number)
			double_digits = True
			if x > 1:
				# print str.format("number[x-2] = {} | last_number = {}", number[x-2], last_number)
				if number[x-2] == last_number:
					double_digits = False
					# print "skipping to next step in loop"
					last_number = number[x]
					continue
			if x < 5:
				double_digits = number[x] != number[x+1]
				# print str.format("double_digits: {}", double_digits)
			if double_digits:
				# print "at least one valid double digits group!"
				break
		last_number = number[x]

	last_number = number[0]
	for x in xrange(1,len(number)):
		if int(number[x]) < int(last_number):
			# print "decreasage!"
			never_decreases = False
			break
		last_number = number[x]

	return double_digits and never_decreases

count = 0
countb = 0
for x in xrange(start,end + 1):
	if valid(str(x)):
		count += 1
	if valid4b(str(x)):
		countb += 1

print "4A | valid inputs: " + str(count)
print "4B | valid inputs: " + str(countb)

# print "test 112233: " + str(valid4b('112233') )
# print "test 123444: " + str(valid4b('123444') )
# print "test 223333: " + str(valid4b('223333') )
# print "test 111122: " + str(valid4b('111122') )

