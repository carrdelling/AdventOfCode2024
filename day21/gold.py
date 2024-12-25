from functools import lru_cache

NUM_PAD = {
    '7': 0, '8': 1, '9': 2,
    '4': 1j, '5': 1 + 1j, '6': 2 + 1j,
    '1': 2j, '2': 1 + 2j, '3': 2 + 2j,
    ' ': 3j, '0': 1 + 3j, 'A': 2 + 3j
}

DIR_PAD = {
    ' ': 0, '^': 1, 'A': 2,
    '<': 1j, 'v': 1 + 1j, '>': 2 + 1j
}

LAYERS = 26


@lru_cache
def find_path(start, end):

    if start in NUM_PAD and end in NUM_PAD:
        pad = NUM_PAD
    else:
        pad = DIR_PAD

    diff = pad[end] - pad[start]
    dx, dy = int(diff.real), int(diff.imag)

    h_moves = ("<" * -dx) + (">" * dx)
    v_moves = ("^" * -dy) + ("v" * dy)

    bad = pad[" "] - pad[start]
    do_vertical = (dx > 0 or bad == dx) and bad != dy * 1j

    moves = v_moves + h_moves if do_vertical else h_moves + v_moves

    return moves + "A"


@lru_cache
def input_code(code, layer, s=0):

    if layer == 0:
        return len(code)

    for i, c in enumerate(code):
        path = find_path(code[i - 1], c)
        s += input_code(path, layer - 1)

    return s


def solve(data):

    codes = data

    complexities = []
    for code in codes:

        steps = input_code(code, LAYERS)

        sign = int(code[:3])
        comp = steps * sign
        complexities.append(comp)

    output = sum(complexities)

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
