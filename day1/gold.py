from collections import Counter


def solve(data):

    a = [d[0] for d in data]
    b = Counter([d[1] for d in data])

    c = [x * b[x] for x in a]
    output = sum(c)

    return output


def main():

    input_ = []
    with open('input') as in_f:
        for row in in_f:
            v = row.strip()
            input_.append(tuple(map(int, v.split())))

    solution = solve(input_)

    print(solution)


if __name__ == "__main__":

    main()


