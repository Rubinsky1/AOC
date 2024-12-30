with open('dag3.txt', 'r') as file:
    data = file.read()


x = 0
y = 0
visited = set()
visited.add((x, y))
for i in range(len(data)):
    if data[i] == '^':
        y += 1
    elif data[i] == 'v':
        y -= 1
    elif data[i] == '>':
        x += 1
    elif data[i] == '<':
        x -= 1
    visited.add((x, y))

print("deel 1:", len(visited))
x = 0
y = 0
xrobot = 0
yrobot = 0
visited = set()
visited.add((x, y))
for i in range(len(data) // 2):
    if data[2 * i] == '^':
        y += 1
    elif data[2 * i] == 'v':
        y -= 1
    elif data[2 * i] == '>':
        x += 1
    elif data[2 * i] == '<':
        x -= 1
    visited.add((x, y))
    if data[2 * i + 1] == '^':
        yrobot += 1
    elif data[2 * i + 1] == 'v':
        yrobot -= 1
    elif data[2 * i + 1] == '>':
        xrobot += 1
    elif data[2 * i + 1] == '<':
        xrobot -= 1
    visited.add((xrobot, yrobot))
print("deel 2:", len(visited))