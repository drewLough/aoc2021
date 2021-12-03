def readInput():
    inputFile = "input.txt"
    f = open(inputFile, "r")
    inputList = f.read().splitlines()
    f.close
    commands = []
    for line in inputList:
        splitInput = line.split()
        command = (splitInput[0], int(splitInput[1]))
        commands.append(command)
    return commands


def calcCoords(commands):
    coords = [0, 0]
    for c in commands:
        if c[0] == "forward":
            coords[0] += c[1]
        elif c[0] == "down":
            coords[1] += c[1]
        elif c[0] == "up":
            coords[1] -= c[1]
    return coords


def calcCoords2(commands):
    x, y = 0, 0
    for c in commands:
        direction = c[0]
        amount = c[1]
        if direction == "forward":
            x += amount
        elif direction == "down":
            y += amount
        elif direction == "up":
            y -= amount
    return [x, y]


def calcFinal(coords):
    return coords[0] * coords[1]


print(calcCoords2(readInput()))
print(calcFinal(calcCoords2(readInput())))
