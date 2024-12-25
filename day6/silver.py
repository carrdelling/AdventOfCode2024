from collections import defaultdict


def next_direction(direction):

    return {
        -1: 1j,
        1j: 1,
        1: -1j,
        -1j: -1,
    }[direction]


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

    gone = False
    count = 0
    while not gone:

        count += 1
        npos = gpos + gdir

        while area[npos] == '#':
            gdir = next_direction(gdir)
            npos = gpos + gdir

        if area[npos] == '$':
            gone = True

        if area[npos] == '.':
            area[npos] = 'X'

        gpos = npos

    output = sum(1 for x in area.values() if x == 'X')

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


