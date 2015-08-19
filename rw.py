import sys

def get_test_cases(fname):
    fp = open(fname, 'r')
    testCaseCount = int(fp.readline())

    for tests in range(0, testCaseCount):
        line = fp.readline()
	rline = reverse_word_seq(line)
	#print 'Original: {0}|Reversed: {1}'.format(line.strip(), rline)
	print 'Case #{0}: {1}'.format(tests+1, rline)

    fp.close() 

def reverse_word_seq(line):
    words = line.split(' ')
    rlineA = []
    rline = ''
    wordCount = len(words)
    #print '{0}:{1}'.format(wordCount, line)
    for itr in range(wordCount-1, -1, -1):
	rlineA.append(words[itr].rstrip())
	#print '{0}: {1}: {2}'.format(itr, words[itr].strip(), rlineA)

    rline = ' '.join(rlineA)
    return rline

get_test_cases(sys.argv[1])
