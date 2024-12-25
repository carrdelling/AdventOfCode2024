from collections import defaultdict

CHEAT = 2
SAVE = 100


def directions(x, y):

    yield x, y + 1
    yield x + 1, y
    yield x, y - 1
    yield x - 1, y


def find_path(area, start):

    path = [start]
    while area[path[-1]] != 'E':

        current = path[-1]
        area[current] = '#'

        for pos in directions(*current):
            if area[pos] in ('.', 'E'):
                path.append(pos)
                break

    return path


def solve(data):

    area = defaultdict(lambda: '#')
    start = 0, 0
    for i, row in enumerate(data):
        for j, c in enumerate(row):

            if c == 'S':
                start = i, j
            area[i, j] = c

    path = find_path(area, start)
    n = len(path)

    cheats = set()
    for p in range(n):

        if (n - p) < SAVE + 1:
            continue

        a = path[p]
        for pp in range(p + SAVE + 1, n):

            b = path[pp]
            dist = abs(a[0] - b[0]) + abs(a[1] - b[1])

            if dist <= CHEAT:
                savings = pp-p - dist
                if savings >= SAVE:
                    cheats.add((savings, p, pp))

    output = len(cheats)

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
