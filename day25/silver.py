from itertools import product


def parse_schemes(data):

    keys = []
    locks = []

    scheme = []
    x = 0
    is_key = False
    for row in data:

        if len(row) < 2:
            x = 0
            continue

        if x == 0:
            if row[0] == '.':
                is_key = True
                scheme = [5] * 5
            else:
                is_key = False
                scheme = [0] * 5
        elif x > 5:
            if is_key:
                keys.append(list(scheme))
            else:
                locks.append(list(scheme))
            continue
        else:
            if is_key:
                for y, c in enumerate(row):
                    if c == '.':
                        scheme[y] = 5 - x
            else:
                for y, c in enumerate(row):
                    if c == '#':
                        scheme[y] = x
        x += 1

    return keys, locks


def solve(data):

    keys, locks = parse_schemes(data)

    valid_pairs = 0
    for k, l in product(keys, locks):
        merged = max([sum(a) for a in zip(k, l)])
        if merged < 6:
            valid_pairs += 1

    output = valid_pairs

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
