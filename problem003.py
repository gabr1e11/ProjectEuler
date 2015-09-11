
import argparse
import math

def find_prime(number):
    i = 2
    while i<number:
        if number%i==0:
            return i
        i += 1
    return number

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 3 of Euler Project')
    parser.add_argument('--number', type=int, default=600851475143)
    args = parser.parse_args()

    number = args.number
    max_prime = 0
    while number != 1:
        prime = find_prime(number)
        number = number/prime

        if prime>max_prime:
            max_prime = prime

    print 'Total is: ',max_prime


