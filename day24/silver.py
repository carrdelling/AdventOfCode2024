

def solve(data):

    gates = []
    values = {}
    for row in data:
        if len(row) < 3:
            continue
        if '->' in row:
            a, g, b, _, c = row.split()
            gates.append((a, b, g, c))
            continue

        i, o = row.split(": ")
        values[i] = int(o)

    changed = True
    while changed:
        changed = False

        for a, b, g, c in gates:
            if c in values:
                continue

            if a in values and b in values:
                res = {
                    'AND': values[a] & values[b],
                    'XOR': values[a] ^ values[b],
                    'OR':  values[a] | values[b],
                }[g]
                values[c] = res
                changed = True

    outs = sorted([(int(c[1:]), v) for c, v in values.items() if c.startswith('z')])[::-1]
    number = int(''.join([str(c[1]) for c in outs]), 2)

    output = number

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
