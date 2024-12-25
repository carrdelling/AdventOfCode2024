import re


def solve(data):

    pattern = re.compile(r"mul\((-?\d+),(-?\d+)\)|(do)\(\)|(don't)\(\)")

    full_text = ''.join(data)
    matches = re.findall(pattern, full_text)

    enabled = 1
    acum = 0
    for match in matches:

        if match[0]:
            mult = int(match[0]) * int(match[1]) * enabled
            acum += mult
        elif match[2] == 'do':
            enabled = 1
        elif match[3] == "don't":
            enabled = 0
        else:
            continue

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
