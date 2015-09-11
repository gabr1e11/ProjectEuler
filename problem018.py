import argparse
import math

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 17 of Euler Project')
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    grid = [[int(num) for num in row.split(' ')] for row in open(args.file).read().split('\n') if row != '']

    nodes = [0 for elem in grid[len(grid)-1]]
    item = 0
    for depth in reversed(range(1, len(grid))):
        level = grid[depth] 
        next_nodes = []
        for item in range(0, len(level)-1):
            next_nodes.append(max(level[item]+nodes[item], level[item+1]+nodes[item+1]))
        nodes = next_nodes
    print nodes[0]+grid[0][0]
