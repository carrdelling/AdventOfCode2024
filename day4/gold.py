from collections import defaultdict


def xmas(i, j, area):

    corners_1 = [
        (i - 1, j - 1),
        (i + 1, j + 1),
    ]

    corners_2 = [
        (i + 1, j - 1),
        (i - 1, j + 1),
    ]

    found = set()
    for ii, jj in corners_1:
        found.add(area[ii, jj])

    if sorted(found) != ['M', 'S']:
        return 0

    found = set()
    for ii, jj in corners_2:
        found.add(area[ii, jj])

    if sorted(found) != ['M', 'S']:
        return 0

    return 1


def solve(data):

    counter = 0
    area = defaultdict(lambda: '.')

    for i, row in enumerate(data):
        for j, c in enumerate(row):
            area[i, j] = c

    targets = [k for k, v in area.items() if v == 'A']

    for i, j in targets:
        print(i, j, counter)
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
