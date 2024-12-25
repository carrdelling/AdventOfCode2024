
def decreasing(x):

    for a, b in zip(x, x[1:]):
        if a <= b:
            return False

    return True


def increasing(x):
    for a, b in zip(x, x[1:]):
        if b <= a:
            return False

    return True


def differ(x):
    for a, b in zip(x, x[1:]):
        if abs(a - b) > 3:
            return False

    return True


def is_valid(report):

    direction = increasing(report) or decreasing(report)
    diff = differ(report)

    return direction and diff


def maybe_valid(report):

    for idx in range(len(report) + 1):

        r = report[:idx] + report[idx+1:]
        if is_valid(r):
            return True

    return False


def solve(data):

    safe = [report for report in data if maybe_valid(report)]
    output = len(safe)

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
