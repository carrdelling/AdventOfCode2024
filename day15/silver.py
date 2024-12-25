from collections import defaultdict


directions = {
    '>': (0, 1),
    'v': (1, 0),
    '<': (0, -1),
    '^': (-1, 0)
}


def parse(data):

    area = defaultdict(lambda: '#')

    idx = 0
    rx, ry = 0, 0
    for row in data:

        if len(row) < 5:
            break
        for j, c in enumerate(row):
            area[idx, j] = c

            if c == '@':
                rx, ry = idx, j

        idx += 1

    moves = ''.join(data[idx+1:]).strip()

    return area, moves, rx, ry


def try_move(x, y, area, mov):

    if area[x, y] == '#':
        return False

    if area[x, y] == '.':
        return True

    # if there is a box
    dx, dy = directions[mov]

    nx = x + dx
    ny = y + dy
    if try_move(nx, ny, area, mov):
        area[nx, ny] = area[x, y]
        area[x, y] = '.'
        return True

    return False


def solve(data):

    area, moves, rx, ry = parse(data)

    for mov in moves:
        dx, dy = directions[mov]

        nx = rx + dx
        ny = ry + dy
        if try_move(nx, ny, area, mov):
            area[nx, ny] = '@'
            area[rx, ry] = '.'
            rx, ry = nx, ny

    output = sum(100*i + j for (i, j), v in area.items() if v == 'O')

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
