
MAX_X = 103
MAX_Y = 101

MAX_STEPS = 100


def solve(data):

    state = []
    for row in data:

        p, v = row.split()
        y, x = map(int, p.split('=')[-1].split(','))
        j, i = map(int, v.split('=')[-1].split(','))

        state.append([x, y, i, j])

    # sim
    step = 0

    while step < MAX_STEPS:
        step += 1

        for r in range(len(state)):

            state[r][0] = ((state[r][0] + state[r][2]) + MAX_X) % MAX_X
            state[r][1] = ((state[r][1] + state[r][3]) + MAX_Y) % MAX_Y

    # quadrants
    mid_x = MAX_X // 2
    mid_y = MAX_Y // 2

    counts = [0, 0, 0, 0]
    for x, y, _, _ in state:

        if x < mid_x:
            if y < mid_y:
                counts[0] += 1
            elif y > mid_y:
                counts[1] += 1
        elif x > mid_x:
            if y < mid_y:
                counts[2] += 1
            elif y > mid_y:
                counts[3] += 1

    output = counts[0] * counts[1] * counts[2] * counts[3]

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
