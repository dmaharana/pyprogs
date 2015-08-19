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
    alphaNum = { 'a':'2', 'b':'22', 'c':'222',
                 'd':'3', 'e':'33', 'f':'333',
		 'g':'4', 'h':'44', 'i':'444',
		 'j':'5', 'k':'55', 'l':'555',
		 'm':'6', 'n':'66', 'o':'666',
		 'p':'7', 'q':'77', 'r':'777', 's':'7777',
		 't':'8', 'u':'88', 'v':'888',
		 'w':'9', 'x':'99', 'y':'999', 'z':'9999',
		 '':'0'
    }
    numS = ''
    for letter in line:
	letter = letter.rstrip()
	#print '{0}: {1}: {2}'.format(line, letter, alphaNum[letter])
	if numS:
	   #print numS
	   lastChar = numS[-1]
	   if lastChar in alphaNum[letter]:
	      numS = numS + ' ' + alphaNum[letter]
	   else:
	      numS = numS + alphaNum[letter]
	else:
	    numS = alphaNum[letter]
	#print '{0}: {1}: {2}'.format(itr, words[itr].strip(), rlineA)

    return numS[:-1]

get_test_cases(sys.argv[1])
