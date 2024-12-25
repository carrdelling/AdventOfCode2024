from functools import lru_cache

BLINKS = 25


def blink(s):

    if s == 0:
        return [1]
    str_s = str(s)

    len_s = len(str_s)
    if len_s % 2 == 0:
        h = len_s // 2
        return [int(str_s[:h]), int(str_s[h:])]

    return [s * 2024]


@lru_cache(maxsize=100_000)
def evolve(s, t):

    step = blink(s)
    if t == BLINKS:
        return len(step)

    if len(step) == 1:
        return evolve(step[0], t+1)

    return evolve(step[0], t + 1) + evolve(step[1], t+1)


def solve(data):

    stones = list(map(int, data[0].split()))

    size = 0

    for s in stones:
        size += evolve(s, 1)

    output = size

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
