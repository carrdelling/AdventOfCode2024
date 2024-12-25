

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
    current_file = file_id - 1

    seek_end = len(memory) - 1
    while current_file > -1:

        # find file
        while memory[seek_end] != current_file:
            seek_end -= 1
        seek_start = seek_end
        while seek_start > -1 and (memory[seek_start] == current_file):
            seek_start -= 1
        else:
            seek_start += 1

        file_size = seek_end - seek_start + 1

        # find space
        seek_space = 0
        space_size = 0
        while space_size < file_size:
            if seek_space >= seek_start:
                break

            while (seek_space < seek_start) and (memory[seek_space] != -1):
                seek_space += 1
            space_end = seek_space
            while (space_end < seek_start) and (memory[space_end] == -1):
                space_end += 1

            space_size = space_end - seek_space if space_end <= seek_start else -1
            if space_size < 0:
                break
            elif space_size < file_size:
                seek_space = space_end + 1
        # move file
        if space_size >= file_size:
            for i in range(seek_start, seek_end + 1):
                memory[i] = -1
            for i in range(file_size):
                memory[seek_space + i] = current_file

        current_file -= 1

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
