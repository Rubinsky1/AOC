
with open("dag10.txt", 'r') as file:
    # Elke regel wordt een lijst van karakters
    pipe_map = [list(regel.strip()) for regel in file]

for x in range(len(pipe_map)):  # Loop door rijen
    for y in range(len(pipe_map[0])):  # Loop door kolommen
        if pipe_map[x][y] == 'S':
            start_x, start_y = x,y
            break
print(start_x, start_y)
# Directions for each pipe type
directions = {
    '|': [(1, 0), (-1, 0)],  # North/South
    '-': [(0, 1), (0, -1)],  # East/West
    'L': [(-1, 0), (0, 1)],  # North/East
    'J': [(-1, 0), (0, -1)], # North/West
    '7': [(1, 0), (0, -1)],  # South/West
    'F': [(1, 0), (0, 1)],   # South/East
    'S': [(1, 0), (-1, 0), (0, 1), (0, -1)]  # S is flexible but connects only where valid
}
# Breadth-first search to find all tiles in the loop and distances
visited = set()
distances = {}

queue = [(start_x, start_y, 0)]  # (x, y, distance)

while queue:
    x, y, dist = queue.pop(0)
    
    # Mark the current tile as visited and store its distance
    if (x, y) in visited:
        continue
    visited.add((x, y))
    distances[(x, y)] = dist

    # Check possible connections from the current pipe
    current_pipe = pipe_map[x][y]
    if current_pipe in directions:
        for dx, dy in directions[current_pipe]:
            nx, ny = x + dx, y + dy

            # Check bounds and validity of the next tile
            if 0 <= nx < len(pipe_map) and 0 <= ny < len(pipe_map[0]) and (nx, ny) not in visited:
                next_pipe = pipe_map[nx][ny]
                # Ensure the next pipe has a valid connection back to the current pipe
                if (-dx, -dy) in directions.get(next_pipe, []):
                    queue.append((nx, ny, dist + 1))

# Find the farthest distance
farthest_distance = max(distances.values())

# Print distances
print("Distances from S:")
for x in range(len(pipe_map)):
    for y in range(len(pipe_map[0])):
        if (x, y) in distances:
            print(distances[(x, y)], end="")
        else:
            print(".", end="")
    print()

print("\nFarthest distance from S:", farthest_distance)