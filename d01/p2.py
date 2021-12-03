def readSums(inputs):
    sums = []
    for i in range(len(inputs) - 2):
        sum = int(inputs[i]) + int(inputs[i+1]) + int(inputs[i+2])
        sums.append(sum)
    return sums


def countIncreases(inputs):
    previous = 0
    count = 0
    for i in range(len(inputs)):
        if i == 0:
            previous = 0
        else:
            if int(inputs[i]) > int(previous):
                count += 1
            previous = inputs[i]
    return count


f = open("input.txt", "r")
input = f.read().splitlines()
f.close

print(readSums(input))
print(countIncreases(readSums(input)))
