from collections import defaultdict


def directions(x, j):

    yield x - 1, j, 'U'
    yield x + 1, j, 'D'
    yield x, j + 1, 'R'
    yield x, j - 1, 'L'


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

        states = {key}
        sides = defaultdict(set)

        while states:

            current = states.pop()
            visited.add(current)
            size += 1

            for x, y, d in directions(*current):

                if area[x, y] != tag:
                    sides[d].add((x, y))

                elif (x, y) not in visited:
                    states.add((x, y))
        else:
            # calculate perimeter
            perimeter = 0

            for d, places in sides.items():
                if d in ('L', 'R'):

                    while places:
                        c = places.pop()
                        perimeter += 1

                        cx, cy = c
                        while (cx - 1, cy) in places:
                            cx -= 1
                            places.remove((cx, cy))

                        cx, cy = c
                        while (cx + 1, cy) in places:
                            cx += 1
                            places.remove((cx, cy))

                if d in ('U', 'D'):
                    while places:
                        c = places.pop()
                        perimeter += 1

                        cx, cy = c
                        while (cx, cy - 1) in places:
                            cy -= 1
                            places.remove((cx, cy))

                        cx, cy = c
                        while (cx, cy + 1) in places:
                            cy += 1
                            places.remove((cx, cy))

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
