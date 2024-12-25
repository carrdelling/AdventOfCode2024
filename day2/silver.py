
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


def solve(data):

    inc = {report for report in data if increasing(report)}
    desc = {report for report in data if (report not in inc) and (decreasing(report))}
    safe = inc | desc
    safe = [report for report in safe if differ(report)]

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


