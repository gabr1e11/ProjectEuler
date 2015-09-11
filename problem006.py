
import argparse
import collections
import math
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 6 of Euler Project')
    parser.add_argument('--limit', type=int, default=100)
    args = parser.parse_args()

    sum_of_squares = 0
    square_of_sums = 0
    for i in xrange(1,args.limit+1):
        sum_of_squares += i*i
        square_of_sums += i

    square_of_sums = square_of_sums*square_of_sums

    print square_of_sums-sum_of_squares
