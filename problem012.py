
import argparse
import math
import collections
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 12 of Euler Project')
    parser.add_argument('--limit', type=int, default=5)
    args = parser.parse_args()

    i=1
    value = 0
    while True:
        value+=i
        primes = collections.Counter(euler.factorize_primes(value))
        divisors = 1
        for k,v in primes.most_common():
            divisors *= v+1
        if divisors>=args.limit:
            print value
            break
        i+=1

