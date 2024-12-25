from collections import defaultdict

ITERATIONS = 2000
PRUNE = 16777216


def solve(data):

    secrets = [int(d) for d in data]

    strategies = defaultdict(int)

    for s in secrets:
        series = {}
        ts = [0, 0, 0, 0]
        for i in range(ITERATIONS):

            old_price = s % 10

            s = (s ^ (s << 6)) % PRUNE
            s = (s ^ (s >> 5)) % PRUNE
            s = (s ^ (s << 11)) % PRUNE

            new_price = s % 10
            delta = new_price - old_price

            ts = ts[1:] + [delta]

            if i > 2:
                tts = tuple(ts)
                if tts not in series:
                    series[tts] = new_price

        for ts in series:
            strategies[ts] += series[ts]

    output = max(strategies.values())

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
