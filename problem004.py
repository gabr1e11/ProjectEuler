
import argparse
import math

def check_palindrome(number):
    number_str = str(number)
    length = len(number_str)

    for j in range(length/1):
        if number_str[j] != number_str[length-1-j]:
            return False
    return True

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 3 of Euler Project')
    parser.add_argument('--limit', type=int, default=1000)
    args = parser.parse_args()

    i = args.limit
    max_i = 0
    max_j = 0
    max_palindrome = 0

    for i in range(args.limit):
        for j in range(i):
            check = i*j
            if check_palindrome(check):
                if check > max_palindrome:
                    max_i = i
                    max_j = j
                    max_palindrome = check

    print 'Number is: %d (%d * %d)' % (max_palindrome, max_i, max_j)


