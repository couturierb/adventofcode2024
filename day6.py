from itertools import cycle

lab = [list(line.strip()) for line in open("day6.input")]
guard = [(index, line.index("^"))for index, line in enumerate(lab) if "^" in line][0]
direction_cycle = cycle([(-1, 0), (0, 1), (1, 0), (0, -1)])
direction = next(direction_cycle)

while True :
    if guard[0]+direction[0] < 0 or guard[0]+direction[0] >= len(lab) or guard[1]+direction[1] < 0 or guard[1]+direction[1] >= len(lab[0]) :
        lab[guard[0]][guard[1]] = "X"break
     
    if lab[guard[0] + direction[0]][guard[1] + direction[1]] == "#" :
        direction = next(direction_cycle)
    else :
        lab[guard[0] + direction[0]][guard[1] + direction[1]] = "^"
        lab[guard[0]][guard[1]] = "X"
        guard = (guard[0] + direction[0], guard[1] + direction[1])

print("part 1 : " + str(sum([line.count("X") for line in lab])))