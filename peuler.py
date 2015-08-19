import math
from timeit import default_timer as timer

#added a comment

def primes2(n):
    pcount = 0
    num = 3

    while pcount != n:
          divisor = 3
	  while math.pow(divisor, 2) <= num and math.fmod(num, divisor) != 0:
	     divisor += 2
	
	  if math.pow(divisor, 2) > num:
	     print 'prime:', num
	     pcount += 1

	  num += 2

    print '%s prime is: %s' % (pcount, num-2)

def primes(n):
    pcount = 0

    for num in range(3, n, 2):
        divisor = 3
	while math.pow(divisor, 2) <= num and math.fmod(num, divisor) != 0:
	   divisor += 2
	
	if math.pow(divisor, 2) > num:
	   print divisor, 'prime:', num
	   pcount += 1

    print 'Number of primes:', pcount

def fib_series_sum(lim):
    n_2 = 1
    n_1 = 2
    n = n_1 + n_2
    sum = 0
    #print n_2, n_1, n

    if n_2 % 2 == 0:
       sum += n_2
       #print n_2

    if n_1 % 2 == 0:
       sum += n_1
       #print n_1

    if n % 2 == 0:
       sum += n
       #print n

    while n < lim:
	  n_2 = n_1
	  n_1 = n
          n = n_1 + n_2
	  if n > lim:
	     break
	  else: 
	     if n % 2 == 0:
		sum += n
	        #print n
	     #print n_2, n_1, n
    print sum

def sum_mul_3_5(num):
    sum = 0
    for num3 in range(0, num, 3):
        sum += num3

    print '3s', sum

    for num5 in range(0, num, 5):
        sum += num5

    for num15 in range(0, num, 15):
        sum -= num15

    print sum
    return sum

def sum_mul_3_5_v2(num):
    n3 = (num - 1) / 3
    print n3

    n5 = (num - 1) / 5
    print n5

    n15 = (num - 1) / 15
    print n15
    sum = (3 * n3 * (n3 + 1)/2) + (5 * n5 * (n5 + 1)/2) - (15 * n15 * (n15 + 1)/2)

    print sum

def prime_factors(num):
    while num % 2 == 0:
       num /= 2
       print 2

    pf = 3
    while pf <= math.sqrt(num):
          while num % pf == 0:
	     num /= pf
	     print pf
          pf += 2

    if num > 2:
       print num

def palindrome (num):
    numL = []
    rc = 0
    for i in str(num):
        numL.append(i)
    #print numL
    #print numL[::-1]
    if numL == (numL[::-1]):
       #print numL, 'equals', numL[::-1]
       rc = 1
    else:
       #print numL, 'NOT equals', numL[::-1]
       rc = 0
    return rc

def find_prod():
    prod = 0
    res_lis = [0]*3
    for num1 in range(111,999):
        for num2 in range(111,999):
	    prod = num1 * num2
	    rc = palindrome(prod)
	    if rc == 1:
	       if prod > res_lis[0]:
                  res_lis = [prod, num1, num2]
    print res_lis

def find_prod2():
    prod = 0
    res_lis = [0]*3
    for num1 in range(999,111,-1):
        for num2 in range(999,111,-1):
	    prod = num1 * num2
	    rc = palindrome(prod)
	    if rc == 1:
	       if prod > res_lis[0]:
                  res_lis = [prod, num1, num2]

    print res_lis

def find_GCD(a, b):
    while a != b:
          if a > b:
	     a -= b
	  else:
	     b -= a
    return a

def find_LCM(a, b):
    return a * b/find_GCD(a, b)
        
def find_multiple():
    num = 0
    lcm = 1
    for num in range(2, 11):
        lcm = find_LCM(lcm, num)
    print 'LCM =', lcm
	
def diff_sqOfsum_sumOfsq(num):
    # square of sum of first n natural numbers: (n * (n + 1) / 2) ** 2
    # sum of square of first n natural numbers: (n * (n + 1) * (2n + 1)/6) = (n ** 3) / 3 + (n ** 2) / 2 + n / 6

    diff = num ** 4 / 4 + num ** 3 / 6 - num ** 2 / 4 - num / 6
    print num, diff

t0 = timer()
primes2(10001)
t1 = timer()
print 'Elapsed time:', t1 - t0
#diff_sqOfsum_sumOfsq(100)
#find_multiple()
#palindrome(1234)
#prime_factors(600851475143)
#fib_series_sum(4000000)
#sum_mul_3_5(1000)
#sum_mul_3_5_v2(1000)
