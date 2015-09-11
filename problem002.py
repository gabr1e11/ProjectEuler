
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 2 of Euler Project')
    parser.add_argument('--limit', type=int, default=4000000, required=True)
    args = parser.parse_args()

    total = 0
    cur = 1
    prev = 0

    while cur <= args.limit:
        tmp = cur
        cur = cur + prev
        prev = tmp
        if cur % 2 == 0:
            total = total + cur

    print 'Total is: ',total


