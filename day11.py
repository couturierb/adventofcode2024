from utils import flat_map_recursive

input_list = open("day11.input").read().split(" ")
input_list = list(map(int, input_list))

# Part 1
def blink(input) :
    if input == 0 :
        return [1]
    elif len(str(input)) % 2 == 0 :
        half = int(len(str(input)) / 2)
        return [int(str(input)[:half]), int(str(input)[half:])]
    else :
        return [input * 2024]

def part1() :
    global input_list
    result = []
    for i in range(25) :
        for input in input_list :
            result += blink(input)
        input_list = result
        result = []
    print("part 1 : " + str(len(input_list)))

# Part 2
map = {
    0 : {"values": [1],"time" : 1},
    1 : {"values" : [2,0,2,4],"time" : 3},
    2 : {"values" : [4,0,4,8],"time" : 3},
    3 : {"values" : [6,0,7,2],"time" : 3},
    4 : {"values" : [8,0,9,6],"time" : 3},
    5 : {"values" : [2,0,4,8,2,8,8,0],"time" : 5},
    6 : {"values" : [2,4,5,7,9,4,5,6],"time" : 5},
    7 : {"values" : [2,8,6,7,6,0,3,2],"time" : 5},
    8 : {"values" : [3,2,7,7,2,6,16192],"time" : 5},
    9 : {"values" : [3,6,8,6,9,1,8,4],"time" : 5}
}

# Tenter plutot de conserver la transformation pour chaque num en X blink
def transform(input, time = 0, max = 75) :
    if (time >= max) :
        return input
    if input > 9 or map[input]["time"] + time > max :
        new_values = blink(input)
        return [transform(v, time+1, max) for v in new_values]
    else :
        return [transform(v, time + map[input]["time"], max) for v in map[input]["values"]]

def part2() :
    result = []
    for input in input_list :
        result += transform(input, 0, 75)
    result = flat_map_recursive(result)
    print("part2 : " + str(len(result)))

# part1()
part2()

