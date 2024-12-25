

def solve(data):

    # parse
    prules = True
    rules = []
    cases = []
    for row in data:

        if len(row) < 2:
            prules = False
            continue

        if prules:
            a, b = map(int, row.split('|'))
            rules.append((a, b))
        elif len(row) > 2:
            c = list(map(int, row.split(',')))

            cc = {v: i for i, v in enumerate(c)}

            m = c[len(c) // 2]
            cases.append((cc, m))

    valid = 0
    for c, m in cases:
        for a, b in rules:

            if c.get(a, -2) > c.get(b, 9999):
                break
        else:
            valid += m

    output = valid

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
