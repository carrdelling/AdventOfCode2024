from statistics import stdev

MAX_X = 103
MAX_Y = 101

MAX_STEPS = 10500


def show(bots):

    print('*' * 110)

    for i in range(105):
        row = []
        for j in range(105):
            row.append('X' if (i, j) in bots else '.')
        print(''.join(row))


def solve(data):

    state = []
    for row in data:

        p, v = row.split()
        y, x = map(int, p.split('=')[-1].split(','))
        j, i = map(int, v.split('=')[-1].split(','))

        state.append([x, y, i, j])

    # sim
    step = 0
    good_step = 0
    while step < MAX_STEPS:
        step += 1

        for r in range(len(state)):

            state[r][0] = ((state[r][0] + state[r][2]) + MAX_X) % MAX_X
            state[r][1] = ((state[r][1] + state[r][3]) + MAX_Y) % MAX_Y

        sx = stdev([x[0] for x in state])
        sy = stdev([x[1] for x in state])
        if sx < 28 and sy < 28:
            bots = {(r[0], r[1]) for r in state}
            print(sx, sy, step)
            good_step = step
            show(bots)

    output = good_step

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
