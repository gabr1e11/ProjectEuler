import argparse
import math
import euler
import itertools
import sys

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--set', type=str, default="0123456789")
    parser.add_argument('--pos', type=int, default=1000000)
    args = parser.parse_args()

    pos = 1
    for perm in itertools.permutations(args.set):
        if pos == args.pos:
            for digit in perm:
                sys.stdout.write(digit)
            break
        pos += 1
    print

