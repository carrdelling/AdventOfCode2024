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
            jj1 = 2 * j
            jj2 = jj1 + 1
            if c == '@':
                area[idx, jj1] = '@'
                area[idx, jj2] = '.'

                rx, ry = idx, jj1
            elif c == 'O':
                area[idx, jj1] = '['
                area[idx, jj2] = ']'
            else:
                area[idx, jj1] = c
                area[idx, jj2] = c

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

    if mov in ('^', 'v'):
        if area[x, y] == '[':
            return try_move(nx, ny, area, mov) and try_move(nx, ny + 1, area, mov)
        elif area[x, y] == ']':
            return try_move(nx, ny, area, mov) and try_move(nx, ny - 1, area, mov)

    else:
        # we try to move the other side of the box first
        return do_move(nx, ny, area, mov)


def do_move(x, y, area, mov):

    if area[x, y] == '#':
        return False

    if area[x, y] == '.':
        return True

    # if there is a box
    dx, dy = directions[mov]
    nx = x + dx
    ny = y + dy

    if mov in ('^', 'v'):
        if area[x, y] == '[':
            if do_move(nx, ny, area, mov) and do_move(nx, ny + 1, area, mov):
                area[nx, ny] = area[x, y]
                area[x, y] = '.'
                area[nx, ny + 1] = area[x, y + 1]
                area[x, y + 1] = '.'
                return True

        elif area[x, y] == ']':
            if do_move(nx, ny, area, mov) and do_move(nx, ny - 1, area, mov):
                area[nx, ny] = area[x, y]
                area[x, y] = '.'
                area[nx, ny - 1] = area[x, y - 1]
                area[x, y - 1] = '.'
                return True

    else:
        if do_move(nx, ny, area, mov):
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
            do_move(nx, ny, area, mov)
            area[nx, ny] = '@'
            area[rx, ry] = '.'
            rx, ry = nx, ny

    output = sum(100*i + j for (i, j), v in area.items() if v == '[')

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
