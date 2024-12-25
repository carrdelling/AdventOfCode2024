import re


def solve(data):

    pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)")

    full_text = ''.join(data)
    matches = re.findall(pattern, full_text)

    acum = 0
    for match in matches:

        mult = int(match[0]) * int(match[1])
        acum += mult

    output = acum

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


