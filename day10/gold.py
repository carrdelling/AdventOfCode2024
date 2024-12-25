from collections import defaultdict


def directions(x, j):

    yield x - 1, j
    yield x + 1, j
    yield x, j + 1
    yield x, j - 1


def explore(start, area):

    trails = [start]
    targets = 0

    while trails:
        i, j = trails.pop()
        land = area[i, j]

        if land == 9:
            targets += 1
            continue

        for x, y in directions(i, j):
            if area[x, y] == (land + 1):
                trails.append((x, y))

    return targets


def solve(data):

    area = defaultdict(lambda: -1)

    trails = []

    for i, row in enumerate(data):
        for j, s in enumerate(row):
            v = int(s)
            area[i, j] = v

            if v == 0:
                t = i, j
                trails.append(t)

    scores = 0
    for trail in trails:
        score = explore(trail, area)
        scores += score

    output = scores

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
