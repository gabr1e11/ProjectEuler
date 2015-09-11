import argparse
import math
import euler
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limitA', type=int, default=1000)
    parser.add_argument('--limitB', type=int, default=1000)
    args = parser.parse_args()

    maxA = args.limitA
    maxB = args.limitB

    # First number that won't be a prime is n=b -> b*b + a*b + b as it
    # is divisible by b. Taking maximum value for a and b will yield
    # the upper limit for the prime search function
    max_value = maxB*maxB + maxA*maxB + maxB

    # Then all the primes up to that maximum value are generated
    primes = euler.first_nth_primes(max_value)
    
    max_sequence = 0
    for a in xrange(-maxA+1, maxA):
        for b in xrange(-maxB+1, maxB):
            #print "Testing %d, %d"% (a, b)
            n=0
            while True:
                if n*n + a*n + b not in primes:
                    break
                n += 1

            if n > max_sequence:
                max_a = a
                max_b = b
                max_sequence = n

    print max_a*max_b
