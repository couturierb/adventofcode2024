import re

machines = []
with open("day13.input") as file :
    arcade = file.read().split('\n\n')
    for machine in arcade :
        matches = re.findall(r'(?<=[XY][+=])\d+', machine)
        machines.append(matches)

def search_better(ax, bx, x) :
    result = []
    little = ax if ax < bx else bx
    for how_many_b in range(int(x/little)) :
        how_many_a = ((x - (bx * how_many_b)) / ax)
        if int(how_many_a) == how_many_a  and int(how_many_a) <= 100 :
            result.append((int(how_many_a), how_many_b, int(how_many_a)*3 + how_many_b))
    return result

def search_better_2(ax, bx, x) :
    result = []
    little = ax if ax < bx else bx
    for how_many_b in range(int(x/little)) :
        how_many_a = ((x - (bx * how_many_b)) / ax)
        if int(how_many_a) == how_many_a :
            result.append((int(how_many_a), how_many_b, int(how_many_a)*3 + how_many_b))
    return result

def part1() :
    total_token = 0
    for m in machines :
        x_possibilities = search_better(int(m[0]), int(m[2]), int(m[4]))
        y_possibilities = search_better(int(m[1]), int(m[3]), int(m[5]))
        l = sorted([i[2] for i in x_possibilities if i in y_possibilities])
        total_token += l[0] if l else 0
    print("part1 : " + str(total_token) + " token")

def part2() :
    total_token = 0
    for m in machines :
        x_possibilities = search_better(int(m[0]), int(m[2]), int(m[4]))
        y_possibilities = search_better(int(m[1]), int(m[3]), int(m[5]))
        l = sorted([i[2] for i in x_possibilities if i in y_possibilities])
        total_token += l[0] if l else 0
    print("part2 : " + str(total_token) + " token")

# part1()
part2() # Perf ! trop compliqué