

def find_gate(i1, i2, g, gates):

    return gates.get((i1, i2, g), gates.get((i2, i1, g)))


def solve(data):

    gates = {}
    values = {}
    for row in data:
        if len(row) < 3:
            continue
        if '->' in row:
            a, g, b, _, c = row.split()
            gates[a, b, g] = c
            continue

        i, o = row.split(": ")
        values[i] = int(o)

    """
        Every digit is an adder logic circuit with the following equations:
        
        X XOR Y  ===> Z
        X AND Y  ====> C1
        
        Z AND lastC ====> C2
        Z XOR lastC ====> ZZ
        C1 OR C2 =====> CC
    
    """

    changed = []

    # 1) Verify y00 XOR x00 -> z00
    assert find_gate('x00', 'y00', 'XOR', gates) == 'z00', f"Bad problem: Digit 0"

    last_carry = ''
    for idx in range(44):
        x = f"x{idx:02d}"
        y = f"y{idx:02d}"
        z = find_gate(x, y, 'XOR', gates)
        c1 = find_gate(x, y, 'AND', gates)
        cc = None   # fill later
        zz = None  # fill later

        # 2) Verify there are no trivial swaps
        assert (z is not None) and (c1 is not None), f"Bad gates at {idx} => Z={z}, C1={c1}"

        # 3) Start seeking problems

        if last_carry != '':
            # check C2
            c2 = find_gate(last_carry, z, 'AND', gates)
            if c2 is None:
                c1, z = z, c1
                changed += [z, c1]
                c2 = find_gate(last_carry, z, 'AND', gates)

            # get final sum
            zz = find_gate(last_carry, z, 'XOR', gates)

            # 1st swap: z <=> zz
            if z is not None and z.startswith("z"):
                z, zz = zz, z
                changed += [z, zz]

            # 2nd swap: c1 <=> zz
            if c1 is not None and c1.startswith("z"):
                c1, zz = zz, c1
                changed += [c1, zz]

            # 3rd swap: c2 <=> zz
            if c2 is not None and c2.startswith("z"):
                c2, zz = zz, c2
                changed += [c2, zz]

            cc = find_gate(c1, c2, 'OR', gates)

        # 4th swap: cc <=> zz
        if last_carry != '' and cc.startswith("z") and cc != f"z{45:02d}":
            cc, zz = zz, cc
            changed += [cc, zz]

        last_carry = c1 if idx == 0 else cc

    output = ','.join(sorted(changed))
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
