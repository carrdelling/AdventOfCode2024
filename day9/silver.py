

def solve(data):

    memory = []

    file_id = 0
    is_file = True
    for c in data[0]:
        if is_file:
            memory += [file_id] * int(c)
            file_id += 1
        else:
            memory += [-1] * int(c)
        is_file = not is_file

    # defrag
    space_ptr = 0
    data_ptr = len(memory) - 1

    while space_ptr < data_ptr:

        while memory[space_ptr] != -1:
            space_ptr += 1
        while memory[data_ptr] == -1:
            data_ptr -= 1

        if space_ptr >= data_ptr:
            break

        memory[space_ptr] = memory[data_ptr]
        memory[data_ptr] = -1

    # checksum
    checksum = sum(idx * v for idx, v in enumerate(memory) if v > 0)
    output = checksum

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
