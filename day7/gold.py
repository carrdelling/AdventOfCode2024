

def check(operands, target, acum):

    if len(operands) < 1:
        return 1 if target == acum else 0

    acum_sum = acum + operands[0]
    v = check(list(operands[1:]), target, acum_sum)

    if v == 1:
        return 1

    acum_prod = acum * operands[0]
    v = check(list(operands[1:]), target, acum_prod)

    if v == 1:
        return 1

    acum_cat = int(f"{acum}{operands[0]}")
    v = check(list(operands[1:]), target, acum_cat)

    return v


def solve(data):

    valid = 0
    for row in data:
        target, rest = row.split(':')
        target = int(target)
        operands = list(map(int, rest.split()))

        test = check(operands[1:], target, operands[0])
        valid += test * target

    output = valid

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
