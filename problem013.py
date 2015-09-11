
import argparse
import math
import collections
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 12 of Euler Project')
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    total = 0
    for number in open(args.file).read().split('\n'):
        if len(number) > 0:
            total += int(number)

    print total
