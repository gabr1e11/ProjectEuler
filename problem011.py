
import argparse
import math
import sets
import euler

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description = 'Solves problem number 11 of Euler Project')
    parser.add_argument('--file', type=str, required=True)
    args = parser.parse_args()

    grid = []
    for row in open(args.file).read().split('\n'):
        if len(row) > 0:
            grid.append(map(lambda elem: int(elem), row.split(' ')))

    max_value = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j<=len(grid[i])-4:
                max_value = max(grid[i][j]*grid[i  ][j+1]*grid[i  ][j+2]*grid[i  ][j+3], max_value)
            if j<=len(grid[i])-4 and i>=3:
                max_value = max(grid[i][j]*grid[i-1][j+1]*grid[i-2][j+2]*grid[i-3][j+3], max_value)
            if j<=len(grid[i])-4 and i<=len(grid)-4:
                max_value = max(grid[i][j]*grid[i+1][j+1]*grid[i+2][j+2]*grid[i+3][j+3], max_value)
            if i<=len(grid)-4:
                max_value = max(grid[i][j]*grid[i+1][j  ]*grid[i+2][j  ]*grid[i+3][j  ], max_value)

    print max_value
