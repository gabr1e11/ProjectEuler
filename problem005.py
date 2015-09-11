
import argparse
import collections
import math
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 5 of Euler Project')
    parser.add_argument('--limit', type=int, default=20)
    args = parser.parse_args()

    final_counter = collections.Counter()
    for i in range(1,args.limit+1):
        primes = euler.factorize_primes(i)
        
        counter = collections.Counter(primes)

        for k,v in counter.most_common():
            # Add the difference
            if v > final_counter[k]:
                final_counter[k] += v-final_counter[k]

    solution = 1
    for k,v in final_counter.most_common():
        solution *= math.pow(k,v)

    solution = int(solution)

    print solution
