import argparse
import math
import sets

def get_divisors(number):
    return [ n for n in range(1, number) if number%n==0 ]

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limit', type=int, default=10)
    args = parser.parse_args()
    
    total = 0
    numbers = sets.Set()

    for a in range(1, args.limit):
        if a not in numbers:
            b = sum(get_divisors(a))
            if a == b:
                continue
            result = sum(get_divisors(b))
            if a == result:
                total += a + b 
                numbers.add(b)
    print total
