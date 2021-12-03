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

# Test Read Func
# print(readInput())


def calcNav(commands):
    horizontal, depth, aim = 0, 0, 0
    for c in commands:
        direction = c[0]
        amount = c[1]
        if direction == "forward":
            horizontal += amount
            depth += amount * aim
        elif direction == "down":
            aim += amount
        elif direction == "up":
            aim -= amount
    print([horizontal, depth])
    return horizontal * depth


print(calcNav(readInput()))
