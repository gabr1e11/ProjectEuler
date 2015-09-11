
import argparse
import math
import euler

def check_number(number, result):
    for m in xrange(2, number):
        for n in xrange(1, number-1):
            a = m*m - n*n
            b = 2*n*m
            c = m*m + n*n
            if a+b+c == result:
                print a*b*c
                return True
    return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 9 of Euler Project')
    parser.add_argument('--result', type=int, default=12)
    args = parser.parse_args()

    i = 3
    while True:
        if check_number(i, args.result):
            break
        i += 1
