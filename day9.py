disk_map = open("day9.input").read()
max_id = int(len(disk_map) / 2)
result = []

ID = 0
for index, value in enumerate(disk_map) :
    value_i = int(value)
    if index % 2 == 0:
        for i in range(value_i) :
            result.append(ID)
        ID += 1
    else :
        for i in range(value_i) :
            result.append(".")

def getLast() :
    value = "."
    while value == "." :
        value = result.pop()
    return value

for index, value in enumerate(result) :
    if not value == "." :
        continue
    result[index] = getLast()

print("part 1 : " + str(sum([int(value) * index for index, value in enumerate(result)])))