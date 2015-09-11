import argparse
import math

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 17 of Euler Project')
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    names = [ (lambda word,pos: sum(ord(ch)-ord('A')+1 for ch in word)*(pos+1))(name,pos) for pos,name in enumerate(sorted(open(args.file).read().replace('\"', '').split(','))) ]

    print sum(names)
