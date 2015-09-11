import argparse
import math
import collections
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 14 of Euler Project')
    parser.add_argument('--limit', type=int, default=14)
    args = parser.parse_args()

    max_terms = 0
    max_number = 0
    for i in xrange(1,args.limit):
        number = i
        nterms = 1
        while number != 1:
            if number%2 == 0:
                number /= 2
            else:
                number = 3*number+1
            nterms += 1

        if nterms>max_terms:
            max_terms = nterms
            max_number = i

    print max_terms, max_number

