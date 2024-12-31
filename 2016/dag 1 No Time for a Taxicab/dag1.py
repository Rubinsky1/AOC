# Open the file in read mode
def read_input(inputfile):
    with open(inputfile, 'r') as file:
        # Read the content of the file
        content = file.read()

    # Split the content by commas and store in an array
    return content.split(', ')

def part1(values):
    x = 0
    y = 0
    direction = 0
    for i in values:
        i = i.strip()
        if i[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        if direction == 0:
            y += int(i[1:])
        elif direction == 1:
            x += int(i[1:])
        elif direction == 2:
            y -= int(i[1:])
        else:
            x -= int(i[1:])

    return(abs(x) + abs(y))

def part2(values):
    x = 0
    y = 0
    direction = 0
    visited = set()
    visited.add((x, y))
    for i in values:
        i = i.strip()
        if i[0] == 'R':
            direction = (direction + 1) % 4
        else:
            direction = (direction - 1) % 4
        if direction == 0:
            for i in range(int(i[1:])):
                y += 1
                if (x, y) in visited:
                    return(abs(x) + abs(y))
                    
                visited.add((x, y))
        elif direction == 1:
            for i in range(int(i[1:])):
                x += 1
                if (x, y) in visited:
                    return(abs(x) + abs(y))
                    
                visited.add((x, y))
        elif direction == 2:
            for i in range(int(i[1:])):
                y -= 1
                if (x, y) in visited:
                    return(abs(x) + abs(y))
                    
                visited.add((x, y))
        else:
            for i in range(int(i[1:])):
                x -= 1
                if (x, y) in visited:
                    return(abs(x) + abs(y))
                    
                visited.add((x, y))
inputfile = 'dag1.txt'
values = read_input(inputfile)
print("deel 1:",part1(values))
print("deel 2:",part2(values))