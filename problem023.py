import argparse
import math
import euler
import sets

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limit', type=int, default=28123)
    args = parser.parse_args()

    abundant = []

    for number in range(1, args.limit):
        sum_div = sum(euler.get_divisors(number))
        if sum_div > number:
            abundant.append(number)

    sum_set = sets.Set()
    for pos, first in enumerate(abundant): 
        for second in abundant[pos:]:
            if first+second<args.limit:
                sum_set.add(first+second)

    total = 0
    for number in range(1, args.limit):
        if number not in sum_set:
            total += number
    
    print total
