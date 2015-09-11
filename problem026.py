import argparse
import math
import euler
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limit', type=int, default=1000)
    args = parser.parse_args()

    maximum = 0
    term = None
    for number in range(2, args.limit):
        cycle = euler.find_cycle(number)
        if cycle > maximum:
            term = number
            maximum = cycle
    print term, maximum
