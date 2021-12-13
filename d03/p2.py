with open('input.txt') as file:
    filedata = [x.strip() for x in file.readlines()]


def oxygen_generator(lines):
    width = len(lines[0])
    rating = lines
    for bit in range(width):
        bit_col = [x[bit] for x in rating]

        if bit_col.count('1') >= bit_col.count('0'):
            rating = [x for x in rating if x[bit] == '1']
        else:
            rating = [x for x in rating if x[bit] == '0']

        if len(rating) == 1:
            break

    return rating


def co2_scrubber(lines):
    width = len(lines[0])
    rating = lines
    for bit in range(width):
        bit_col = [x[bit] for x in rating]

        if bit_col.count('1') >= bit_col.count('0'):
            rating = [x for x in rating if x[bit] == '0']
        else:
            rating = [x for x in rating if x[bit] == '1']

        if len(rating) == 1:
            break

    return rating


oxygen = int(oxygen_generator(filedata)[0], 2)
print("oxygen: " + str(oxygen))
co2 = int(co2_scrubber(filedata)[0], 2)
print("co2: " + str(co2))
print("product: " + str(oxygen * co2))
