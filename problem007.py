
import argparse
import math
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 3 of Euler Project')
    parser.add_argument('--limit', type=int, default=6)
    args = parser.parse_args()

    num_primes = 0
    number = 2
    while True:
        if euler.find_prime(number) == number:
            num_primes += 1
        if num_primes == args.limit:
            break
        number += 1

    print 'Prime number %d is: %d' % (args.limit, number)


