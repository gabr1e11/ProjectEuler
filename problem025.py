import argparse
import math
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 19 of Euler Project')
    parser.add_argument('--limit', type=int, default=1000)
    args = parser.parse_args()

    for pos,fib in enumerate(euler.fibonacci()):
        if fib >= 10**(args.limit-1):
            print pos+1
            break
    
