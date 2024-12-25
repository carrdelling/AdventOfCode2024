

"""

2,4,1,7,7,5,0,3,4,4,1,7,5,5,3,0

b = a % 8
b = b xor 111
c = a // 2** b
a = a // 8
b = b xor c
b = b xor 111
output b%8
if a != 0:
 back to first line

while a != 0:
    b = a % 8
    b = b xor 111
    c = a // 2** b

    b = b xor c
    b = b xor 111
    output b%8

    a = a // 8

Every iteration prints a number.
The number depends on current a only, and uses at most the last 3 digits

"""


def combo(op, a, b, c):

    return {4: a, 5: b, 6: c}.get(op, op)


def do_run(program, a, b, c):

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
                yield combo_val % 8
            case 6:  # bdv
                b = a // (2 ** combo_val)
            case 7:  # cdv
                c = a // (2 ** combo_val)

        ip += 2


def match_code(program, out, old_a=0):

    if len(out) < 1:
        return old_a

    for a in range(1 << 10):
        if (a >> 3) == (old_a & 127):
            next_value = next(do_run(program, a, 0, 0))
            if next_value == out[-1]:
                current_a = match_code(program, out[:-1], (old_a << 3) | (a % 8))

                # only return if we get a good value for the next operand
                if current_a is not None:
                    return current_a


def solve(data):

    program = []

    for row in data:
        chunks = row.split(': ')
        if len(chunks) < 2:
            continue
        if chunks[0] == 'Program':
            program = list(map(int, chunks[1].split(',')))

    output = match_code(program, program)

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
