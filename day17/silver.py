

def combo(op, a, b, c):

    return {4: a, 5: b, 6: c}.get(op, op)


def solve(data):

    program = []
    output = []
    a, b, c = 0, 0, 0

    for row in data:
        chunks = row.split(': ')
        if len(chunks) < 2:
            continue
        if chunks[0] == 'Program':
            program = list(map(int, chunks[1].split(',')))
        if chunks[0] == 'Register A':
            a = int(chunks[1])
        if chunks[0] == 'Register B':
            b = int(chunks[1])
        if chunks[0] == 'Register C':
            c = int(chunks[1])

    ip = 0

    while ip < len(program):

        opcode = program[ip]
        operand = program[ip + 1]
        combo_val = combo(operand, a, b, c)

        match opcode:
            case 0:  # adv
                a = (a // 2 ** combo_val)
            case 1:  # bxl
                b = b ^ operand
            case 2:
                b = combo_val % 8
            case 3:
                if a != 0:
                    ip = operand - 2
            case 4:  # bxc
                b = b ^ c
            case 5:  # out
                output.append(combo_val % 8)
            case 6:  # bdv
                b = a // (2 ** combo_val)
            case 7:  # cdv
                c = a // (2 ** combo_val)

        ip += 2

    final_output = ','.join(map(str, output))

    return final_output


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
