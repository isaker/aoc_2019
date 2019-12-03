filepath = '../input/day2input.txt'

def decode(op_l):
	for x in xrange(0,len(op_l), 4):
		#print 'executing op code ' + str(x)
		if op_l[x] == 99:
			#print 'Final op list: ' + str(op_list)
			return op_l[0]
		elif op_l[x] == 1:
			inp_val1 = op_l[x+1]
			inp_val2 = op_l[x+2]
			res_post = op_l[x+3]
			result = op_l[inp_val1] + op_l[inp_val2]
			op_l[res_post] = result
			#print str(op_list)
		elif op_l[x] == 2:
			inp_val1 = op_l[x+1]
			inp_val2 = op_l[x+2]
			res_post = op_l[x+3]
			result = op_l[inp_val1] * op_l[inp_val2]
			op_l[res_post] = result
			#print str(op_list)
def get_op_list():
	with open(filepath) as f:
	    line = f.readline()

	line = line.rstrip('\n')
	op_list = line.split(',')

	for o in xrange(0,len(op_list)):
		op_list[o] = int(op_list[o])
	return op_list

test_list = get_op_list()
print "test_list: " + str(test_list)
for x in xrange(0,100):
	test_list[1] = x
	for y in xrange(0,100):
		test_list[2] = y
		print "testing noun: " + str(x) + " verb: " + str(y)
		print "test_list: " + str(test_list)
		if decode(test_list) == 19690720:
			print "ANSWER: noun: " + str(x) +  "verb: " + str(y)
			break
		test_list = get_op_list()
		test_list[1] = x

