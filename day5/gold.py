

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
            cases.append((cc, m, c))

    valid = 0
    invalid = []
    for c, m, o in cases:
        for a, b in rules:

            if c.get(a, -2) > c.get(b, 9999):
                invalid.append(c)
                break
        else:
            valid += m

    fixed = 0
    for c in invalid:

        # fix it
        changed = True
        while changed:
            changed = False
            for a, b in rules:
                if c.get(a, -2) > c.get(b, 9999):
                    x = c[a]
                    c[a] = c[b]
                    c[b] = x
                    changed = True

        # find mid value
        mi = len(c) // 2
        v = None
        for k, kk in c.items():
            if kk == mi:
                v = k
                break
        fixed += v

    output = fixed

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
