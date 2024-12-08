import re

def getXLines():
    x_lines = []

    # \\\\
    # .\\\
    # ..\\
    # ...
    for col in range(len(lines[0])) :
        x_lines.append("".join([lines[diag][col+diag] for diag in range(len(lines[0])) if col+diag < len(lines[0]) and diag < len(lines)]))

    # ....
    # \...
    # \\..
    # \\\.
    for row in range(1, len(lines)) :
        x_lines.append("".join([lines[row+diag][diag] for diag in range(len(lines)-row)]))
 

    # ////
    # ///.
    # //..
    # /...
    for col in range(len(lines[0]), 0, -1) :
        x_lines.append("".join([lines[diag][col-1-diag] for diag in range(len(lines[0])) if col-diag > 0 and diag < len(lines)]))

    # ....
    # .../
    # ..//
    # .///
    for row in range(1, len(lines)) :
        x_lines.append("".join([lines[row+diag][len(lines[0])-1-diag] for diag in range(len(lines)-row)]))

    # print(x_lines)
    return x_lines

lines = [line.strip() for line in open("day4.input")]
h_lines = ["".join([elem[i] for elem in lines]) for i in range(len(lines[0]))]
x_lines = getXLines()
regex = r"(?=(XMAS|SAMX))"
occurence = re.findall(regex, ",".join(lines+h_lines+x_lines))
print(len(occurence))
