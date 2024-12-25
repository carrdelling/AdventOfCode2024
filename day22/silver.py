
ITERATIONS = 2000
PRUNE = 16777216


def solve(data):

    secrets = [int(d) for d in data]

    processed = []
    for s in secrets:

        for i in range(ITERATIONS):
            s = (s ^ (s << 6)) % PRUNE
            s = (s ^ (s >> 5)) % PRUNE
            s = (s ^ (s << 11)) % PRUNE

        processed.append(s)

    output = sum(processed)

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
