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


f = open("inputP1.txt", "r")
input = f.read().splitlines()
f.close

print(countIncreases(input))
