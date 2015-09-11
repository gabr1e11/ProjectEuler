import argparse
import math
import collections
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 15 of Euler Project')
    parser.add_argument('--size', type=int, default=2)
    args = parser.parse_args()

    x = math.factorial(2*args.size)
    y = math.factorial(args.size)

    print x/(y*y)

