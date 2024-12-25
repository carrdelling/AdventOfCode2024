

def solve(data):

    a = sorted([d[0] for d in data])
    b = sorted([d[1] for d in data])

    c = [abs(x - y) for x, y in zip(a, b)]
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


