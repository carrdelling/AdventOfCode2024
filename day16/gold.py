from collections import defaultdict


def rot_left(s):
    return {'E': 'N', 'N': 'W', 'W': 'S', 'S': 'E'}[s]


def rot_right(s):
    return {'E': 'S', 'S': 'W', 'W': 'N', 'N': 'E'}[s]


def forward(x, y, d):

    return {
        'E': (x, y + 1),
        'S': (x + 1, y),
        'W': (x, y - 1),
        'N': (x - 1, y),
    }[d]


def solve(data):

    area = defaultdict(lambda: '#')
    start, end = (0, 0), (0, 0)
    direction = 'E'
    for i, row in enumerate(data):
        for j, c in enumerate(row):

            if c == 'S':
                area[i, j] = '.'
                start = i, j
            elif c == 'E':
                area[i, j] = '.'
                end = i, j
            else:
                area[i, j] = c

    states = [(start[0], start[1], direction, 0, {(start[0], start[1])})]
    min_cost = 1_000_000
    visited_min = set()

    seen = {}
    while states:
        x, y, d, c, v = states.pop()
        v.add((x, y))

        if seen.get((x, y, d), 1_000_000) < c:
            continue

        seen[x, y, d] = c

        if (x, y) == end:
            if min_cost > c:
                min_cost = c
                visited_min = set(v)
            elif min_cost == c:
                visited_min |= set(v)
            continue

        if c > min_cost:
            continue

        i, j = forward(x, y, d)

        if area[i, j] == '.':
            states.append((i, j, d, c + 1, set(v)))

        left = rot_left(d)
        fw = forward(x, y, left)

        if area[fw] == '.':
            states.append((x, y, left, c + 1000, set(v)))

        right = rot_right(d)
        fw = forward(x, y, right)

        if area[fw] == '.':
            states.append((x, y, right, c + 1000, set(v)))

    output = len(visited_min)

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
