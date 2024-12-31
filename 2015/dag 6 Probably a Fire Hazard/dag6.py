import sys

def read_input():
    lines = []
    for line in sys.stdin:
        lines.append(line)

    begin = []
    eind = []
    toggle = []

    for i, line in enumerate(lines):
        if i % 3 == 0:
            toggle.append(int(line))
        elif i % 3 == 1:
            x, y = map(int, line.strip().split(','))
            begin.append((x, y))
        else:
            x, y = map(int, line.strip().split(','))
            eind.append((x,y))
    return begin, eind, toggle

def part1(begin, eind, toggle):
    grid = [[False for i in range(1000)] for j in range(1000)]
    for i in range(len(toggle)):
        if toggle[i] == 0:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    grid[x][y] = not grid[x][y]
        if toggle[i] == 1:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    grid[x][y] = True
        if toggle[i] == 2:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    grid[x][y] = False

    count = 0
    for x in range(1000):
        for y in range(1000):
            if grid[x][y]:
                count += 1
    return count

def part2(begin, eind, toggle):
    grid = [[0 for i in range(1000)] for j in range(1000)]
    for i in range(len(toggle)):
        if toggle[i] == 0:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    grid[x][y] += 2
        if toggle[i] == 1:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    grid[x][y] +=1
        if toggle[i] == 2:
            for x in range(begin[i][0], eind[i][0] + 1):
                for y in range(begin[i][1], eind[i][1] + 1):
                    if grid[x][y] > 0:
                        grid[x][y] -= 1

    count = 0
    for x in range(1000):
        for y in range(1000):
            count+= grid[x][y]
    return count

begin, eind, toggle = read_input()
print("deel 1:",part1(begin, eind, toggle))
print("deel 2:",part2(begin, eind, toggle))