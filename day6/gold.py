from collections import defaultdict
from copy import deepcopy


def next_direction(direction):

    return {
        -1: 1j,
        1j: 1,
        1: -1j,
        -1j: -1,
    }[direction]


def check_cycle(area, gdir, gpos, obs):

    _area = deepcopy(area)
    _area[obs] = '#'

    gone = False
    cycle = False
    seen = set()
    count = 0
    while (not gone) and (not cycle):

        if (gpos, gdir) in seen:
            cycle = True
            continue
        seen.add((gpos, gdir))

        count += 1
        npos = gpos + gdir

        count += 1
        while _area[npos] == '#':
            gdir = next_direction(gdir)
            npos = gpos + gdir

        if _area[npos] == '$':
            gone = True

        gpos = npos

    return 1 if cycle else 0


def solve(data):

    area = defaultdict(lambda: '$')

    gdir = -1
    gpos = None
    for i, row in enumerate(data):
        for j, v in enumerate(row):
            pos = complex(int(i), int(j))
            if v == '^':
                gpos = pos
                area[pos] = '.'
            else:
                area[pos] = v

    count = 0
    for k, v in area.items():
        if v == '.' and (k != gpos):
            count += check_cycle(area, gdir, gpos, k)

    output = count

    return output


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


