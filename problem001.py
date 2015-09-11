
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 1 of Euler Project')
    parser.add_argument('--limit', type=int, default=1000, required=True)
    args = parser.parse_args()

    total = 0

    for number in range(args.limit):
        if (number % 3) == 0 or (number % 5) == 0:
            total += number

    print 'Total is: ',total


