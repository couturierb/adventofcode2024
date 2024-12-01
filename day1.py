from functools import reduce

left = []
right = []

with open("day1.input") as file :
    for line in file :
        lineArr = line.split()
        left.append(int(lineArr[0]))
        right.append(int(lineArr[1]))

def part1() :
    left.sort()
    right.sort()
    lists = zip(left, right)
    print(reduce(lambda acc, elem: acc + abs(elem[0] - elem[1]), lists, 0))

def part2() :
    print(reduce(lambda acc, elem: acc + right.count(elem) * elem, left, 0))

# part1()
part2()