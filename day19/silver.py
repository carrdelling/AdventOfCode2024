from functools import lru_cache


@lru_cache
def find_pattern(target, patterns):

    if target == '':
        return 1

    found = 0
    for pat in patterns:
        if target.startswith(pat):
            found += find_pattern(target.removeprefix(pat), patterns)

    return found


def solve(data):

    patterns = tuple(data[0].split(', '))
    targets = data[2:]

    count = 0
    for target in targets:
        times = find_pattern(target, patterns)
        count += min(times, 1)

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
