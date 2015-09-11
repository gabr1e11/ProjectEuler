import argparse
import math
import euler
import itertools

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limitA', type=int, default=1000)
    parser.add_argument('--limitB', type=int, default=1000)
    args = parser.parse_args()

