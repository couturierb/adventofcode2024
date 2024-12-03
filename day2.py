total = 0

def checkLine(line: list[int]) :
    current = line[0]
    direction = None
    for i in line[1:]:
        currentDirection = i-current > 0
        if (abs(i-current) > 3 or i-current == 0 or (not direction == None and not currentDirection == direction)) :
            return False
        direction = currentDirection
        current = i
    print("line ok " + str(line))
    return True

def part1():
    global total
    with open("day2.input") as file :
        for line in file :
            total += 1 if checkLine(list(map(int, line.split()))) else 0
    print(total)


def part2():
    global total
    with open("day2.input") as file :
        for line in file :
            intList = list(map(int, line.split()))
            total += 1 if checkLine(intList) or any(checkLine(intList[:i] + intList[i+1:]) for i in range(len(intList))) else 0
    print(total)

# part1()
part2()