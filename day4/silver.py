from collections import defaultdict


def xmas(i, j, area):

    patterns = [
        (('M', i - 1, j), ('A', i - 2, j), ('S', i - 3, j)),
        (('M', i + 1, j), ('A', i + 2, j), ('S', i + 3, j)),
        (('M', i, j - 1), ('A', i, j - 2), ('S', i, j - 3)),
        (('M', i, j + 1), ('A', i, j + 2), ('S', i, j + 3)),

        (('M', i - 1, j + 1), ('A', i - 2, j + 2), ('S', i - 3, j + 3)),
        (('M', i + 1, j + 1), ('A', i + 2, j + 2), ('S', i + 3, j + 3)),
        (('M', i - 1, j - 1), ('A', i - 2, j - 2), ('S', i - 3, j - 3)),
        (('M', i + 1, j - 1), ('A', i + 2, j - 2), ('S', i + 3, j - 3)),
    ]

    found = 0
    for p in patterns:
        for step in p:
            ii = step[1]
            jj = step[2]
            if area[ii, jj] != step[0]:
                break
        else:
            found += 1

    return found


def solve(data):

    counter = 0
    area = defaultdict(lambda: '.')

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            area[i, j] = c

    targets = [k for k, v in area.items() if v == 'X']

    for i, j in targets:
        counter += xmas(i, j, area)

    output = counter

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
