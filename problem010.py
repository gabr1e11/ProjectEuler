
import argparse
import math
import sets
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 10 of Euler Project')
    parser.add_argument('--limit', type=int, default=10)
    args = parser.parse_args()

    natural = sets.Set(xrange(2,args.limit))

    for i in xrange(2,args.limit):
        product = i*2
        while product < args.limit:
            natural.discard(product)
            product += i

    print sum(natural)
