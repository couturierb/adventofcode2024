import re

data = open("day3.input").read()
mul_regexp = r"mul\(\d+,\d+\)"
mul_and_activate_regexp = r"mul\(\d+,\d+\)|do\(\)|don't\(\)"

def part1() :
    total = 0
    operations = re.findall(mul_regexp, data)
    for op in operations :
        digits = re.findall(r"\d+", op)
        total += int(digits[0]) * int(digits[1])
    print(total)

def part2() :
    total = 0
    activated = True
    operations = re.findall(mul_and_activate_regexp, data)
    for op in operations :
        if "don't" in op :
            activated = False
        elif "do" in op :
            activated = True
        elif activated :
            digits = re.findall(r"\d+", op)
            total += int(digits[0]) * int(digits[1])
    print(total)

# part1()
part2()
