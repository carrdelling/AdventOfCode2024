from itertools import product


def parse(data):

    # Button A: X + 45, Y + 76
    # Button B: X + 84, Y + 14
    # Prize: X = 9612, Y = 4342

    cases = []
    a, b, p = None, None, None
    for row in data:
        if len(row) < 2:
            continue
        c = row.split(':')[-1].split(',')

        if 'Button A' in row:
            a = int(c[0].split('+')[-1]), int(c[1].split('+')[-1])
            continue
        if 'Button B' in row:
            b = int(c[0].split('+')[-1]), int(c[1].split('+')[-1])
            continue
        if 'Prize' in row:
            p = int(c[0].split('=')[-1]), int(c[1].split('=')[-1])

        cases.append((a, b, p))

    return cases


def solve_case(a, b, p):

    MAX_TRIES = 1000
    ax, ay = a
    bx, by = b
    px, py = p

    for ta, tb in product(range(MAX_TRIES), repeat=2):

        if (ta * ax) + (tb * bx) == px:
            if (ta * ay) + (tb * by) == py:
                return 3*ta + tb

    return 0


def solve(data):

    cases = parse(data)

    tokens = 0
    for a, b, p in cases:
        tokens += solve_case(a, b, p)

    output = tokens

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

