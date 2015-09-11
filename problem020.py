import argparse
import math

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limit', type=int, default=10)
    args = parser.parse_args()
    
    total = 0
    for digit in str(math.factorial(args.limit)):
        total += (int(digit))
    print total
