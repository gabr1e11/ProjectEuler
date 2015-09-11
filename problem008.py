
import argparse
import math
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 3 of Euler Project')
    parser.add_argument('--file', type=str, required=True)
    parser.add_argument('--length', type=int, default=5)
    args = parser.parse_args()

    datafile = open(args.file)
    data_str = datafile.read()
    datafile.close()

    max_product = 0
    for i in xrange(0, len(data_str)-args.length):
        product = int(data_str[i]) * int(data_str[i+1]) * int(data_str[i+2]) * int(data_str[i+3]) * int(data_str[i+4])
        if product > max_product:
            max_product = product
    print max_product 


