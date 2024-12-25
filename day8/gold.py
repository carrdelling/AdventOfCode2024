from collections import defaultdict
from itertools import combinations
from math import gcd


def solve(data):

    area = set()
    antenas = defaultdict(list)
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            pos = complex(i, j)
            area.add(pos)
            if v != '.':
                antenas[v].append(pos)

    # I don't like ray tracing problems...
    RAYTRACING = 100
    antinodes = set()
    for label, ants in antenas.items():
        for x, y in combinations(ants, 2):
            dist = x - y

            red = gcd(int(dist.real), int(dist.imag))
            step = dist / red

            # ray trace, ray trace!
            for i in range(-RAYTRACING, RAYTRACING):
                antinodes.add(x + (i * step))

    solution = len(antinodes & area)

    return solution


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(v)

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()
