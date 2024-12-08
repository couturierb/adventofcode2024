lines = [line.strip() for line in open("day8.input")]
antennas = {}
antinodes = set()
antinodes_2 = set()

# Create Antennas dictionnary
for rowIndex, line in enumerate(lines) :
    for colIndex, char in enumerate(line) :
        if (not char == '.') :
            antennas.setdefault(char, {(rowIndex, colIndex)})
            antennas[char].add((rowIndex, colIndex))

def compute_antinodes(point_A: tuple[int, int], point_B: tuple[int, int]):
    x_signe = -1 if point_A[0] <= point_B[0] else 1
    y_signe = -1 if point_A[1] <= point_B[1] else 1
    diff_anntenna = (point_A[0] - point_B[0], point_A[1] - point_B[1])
    antinodes.add((point_A[0] + diff_anntenna[0], point_A[1] + diff_anntenna[1]))
    antinodes.add((point_B[0] - diff_anntenna[0], point_B[1] - diff_anntenna[1]))

def compute_antinodes_2(point_A: tuple[int, int], point_B: tuple[int, int]):
    x_signe = -1 if point_A[0] <= point_B[0] else 1
    y_signe = -1 if point_A[1] <= point_B[1] else 1
    diff_anntenna = (point_A[0] - point_B[0], point_A[1] - point_B[1])

    antinodes_2.add(point_A)
    antinodes_2.add(point_B)
    index = 1
    while True:
        point = (point_A[0] + (diff_anntenna[0] * index), point_A[1] + (diff_anntenna[1] * index))
        if point[0] < 0 or point[1] < 0 or point[0] >= len(lines) or point[1] >= len(lines[0]) :
            break
        antinodes_2.add(point)
        index += 1

    index = 1
    while True:
        point = (point_B[0] - (diff_anntenna[0] * index), point_B[1] - (diff_anntenna[1] * index))
        if point[0] < 0 or point[1] < 0 or point[0] >= len(lines) or point[1] >= len(lines[0]) :
            break
        antinodes_2.add(point)
        index += 1

for antenna in antennas.values():
    for index, antenna_point in enumerate(antenna) :
        for antenna_next_point in list(antenna)[index+1:] :
            compute_antinodes(antenna_point, antenna_next_point)
            compute_antinodes_2(antenna_point, antenna_next_point)

print(antinodes_2)
filtered_antinodes = {a for a in antinodes if a[0] >= 0 and a[1] >= 0 and a[0] < len(lines) and a[1] < len(lines[0])}
filtered_antinodes_2 = {a for a in antinodes_2 if a[0] >= 0 and a[1] >= 0 and a[0] < len(lines) and a[1] < len(lines[0])}

print("part1 : " + str(len(filtered_antinodes)))
print("part2 : " + str(len(filtered_antinodes_2)))