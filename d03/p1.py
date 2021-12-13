with open('input.txt') as f:
    fd = f.readlines()


def gamma(data):
    width = len(data[0]) - 1
    gamma = [0] * width
    for i in range(width):
        count = 0
        for line in data:
            if line[i] == '1':
                count += 1
        if count * 2 > len(data):
            gamma[i] = 1
    return gamma


def gamma2(lines):
    width = len(lines[0])
    gamma = [0] * width
    epsilon = [0] * width
    for i in range(width):
        bit_col = [x[i] for x in lines]

        if bit_col.count('1') > bit_col.count('0'):
            gamma[i] = '1'
            epsilon[i] = '0'
        else:
            gamma[i] = '0'
            epsilon[i] = '1'

    return gamma


def epsilon(gamma):
    epsilon = []
    for bit in gamma:
        val = 1 if bit == 0 else 0
        epsilon.append(val)
    return epsilon


def epsilon2(gamma):
    return [int(not(bit)) for bit in gamma]


def bits_to_int(bits):
    bitString = [str(bit) for bit in bits]
    return int(''.join(bitString), 2)


def countingBinaries(fd):
    g = gamma(fd)
    e = epsilon2(g)
    return bits_to_int(g) * bits_to_int(e)


print(countingBinaries(fd))
print(bits_to_int(gamma2(fd)))
