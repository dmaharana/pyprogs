import sys
import itertools

def get_test_cases(fname):
    fp = open(fname, 'r')
    testCaseCount = int(fp.readline())

    for tests in range(0, testCaseCount):
        numCount = fp.readline().rstrip()
        v1 = fp.readline().rstrip()
        v2 = fp.readline().rstrip()
	prod = min_vector_prod(v1, v2)
	#print 'Original: {0}|Reversed: {1}'.format(line.strip(), rline)
	print 'Case #{0}: {1}'.format(tests+1, prod)

    fp.close() 

def min_vector_prod(v1, v2):
    v1A = v1.split(' ')
    v2A = v2.split(' ')
    prodSum = 0
    newSum = 0
    tempL = []

    for itr in range(len(v1A)):    
        prodSum += (int(v1A[itr]) * int(v2A[itr]))

    #generate combinations
    v1Ac = permutate_vector(v1A)

    #multiply the vectors
    for vect in v1Ac:
        for itr in vect:
	    tempL.append(itr)

	newSum = 0
	for itr in range(len(tempL)):    
            newSum += (int(tempL[itr]) * int(v2A[itr]))
	#print 'tempL = {0}, v2A = {1}, sum = {2}'.format(tempL, v2A, newSum)
        tempL = []

	if newSum < prodSum:
	   prodSum = newSum

    #generate combinations
    v2Ac = permutate_vector(v2A)

    #multiply the vectors
    for vect in v2Ac:
        for itr in vect:
	    tempL.append(itr)

	#print 'vect = {0}, tempL = {1}, v1A = {2}'.format(vect, tempL, v1A)
	newSum = 0
	for itr in range(len(tempL)):    
            newSum += (int(tempL[itr]) * int(v1A[itr]))
	#print 'tempL = {0}, v2A = {1}, sum = {2}'.format(tempL, v1A, newSum)
        tempL = []

	if newSum < prodSum:
	   prodSum = newSum


    return prodSum


def permutate_vector(v1):
    perL = list(itertools.permutations(v1))
    return perL

get_test_cases(sys.argv[1])

#permutate_vector(['a','b','c'])
