from collections import defaultdict


def directions(x, j):

    yield x - 1, j
    yield x + 1, j
    yield x, j + 1
    yield x, j - 1


def solve(data):

    area = defaultdict(lambda: '.')

    visited = set()

    for i, row in enumerate(data):
        for j, s in enumerate(row):
            area[i, j] = s

    prices = []
    for key in list(area):

        if key in visited:
            continue

        tag = area[key]
        size = 0
        perimeter = 0

        states = {key}

        while states:

            current = states.pop()
            visited.add(current)
            size += 1

            for x, y in directions(*current):

                if area[x, y] != tag:
                    perimeter += 1
                elif (x, y) not in visited:
                    states.add((x, y))

        price = size * perimeter
        prices.append(price)

    output = sum(prices)

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
