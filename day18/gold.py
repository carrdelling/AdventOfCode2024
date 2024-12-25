import heapq

SIZE = 71


def moves(x, y):

    yield x, y + 1
    yield x + 1, y
    yield x, y - 1
    yield x - 1, y


def score(x, y):
    return (SIZE - x - 1) + (SIZE - y - 1)


def search(blocks):

    states = [(score(0, 0), 0, 0, 0, set())]
    min_c = {}

    while states:

        current = heapq.heappop(states)
        s, x, y, c, visited = current
        visited.add((x, y))

        if c >= min_c.get((x, y), 1_000_000):
            continue

        min_c[x, y] = c

        for i, j in moves(x, y):
            if (i, j) in blocks:
                continue
            if (i, j) in visited:
                continue
            if i >= SIZE or i < 0 or j >= SIZE or j < 0:
                continue

            heapq.heappush(states, (score(i, j), i, j, c + 1, set(visited)))

    return (SIZE - 1, SIZE - 1) in min_c


def solve(data):

    blocks = set()
    for row in data:
        x, y = map(int, row.split(','))
        blocks.add((x, y))

    output = ''
    for row in data[::-1]:
        x, y = map(int, row.split(','))
        blocks.discard((x, y))

        if search(blocks):
            output = f"{x},{y}"
            break

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
