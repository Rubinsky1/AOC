import sys
import time

def dag8(input, part2=False):

  points = [(int(x), int(y), int(z)) for x, y, z in input]
  n = len(points)


  edges = []
  for i in range(n):
    xi, yi, zi = points[i]
    for j in range(i + 1, n):
      xj, yj, zj = points[j]
      dist2 = (xi - xj) ** 2 + (yi - yj) ** 2 + (zi - zj) ** 2
      edges.append((dist2, i, j))


  edges.sort(key=lambda e: e[0])

  # Union-Find 
  parent = list(range(n))
  size = [1] * n

  def find(a):
    while parent[a] != a:
      parent[a] = parent[parent[a]]
      a = parent[a]
    return a

  def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
      return False
    if size[ra] < size[rb]:
      ra, rb = rb, ra
    parent[rb] = ra
    size[ra] += size[rb]
    return True


  K = 1000
  last = None
  if part2:
    for _, i, j in edges[:len(edges)]:
      if union(i, j):
        last = (i, j)
    return int(input[last[0]][0]) * int(input[last[1]][0])
  if not part2:
    for _, i, j in edges[:min(K, len(edges))]:
      union(i, j)

  comp_sizes = {}
  for i in range(n):
    r = find(i)
    comp_sizes[r] = comp_sizes.get(r, 0) + 1

  largest = sorted(comp_sizes.values(), reverse=True)[:3]
  if len(largest) < 3:
    return 0
  answer = largest[0] * largest[1] * largest[2]
  return answer

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  input = ([[char for char in line.strip().split(',')] for line in lines])

  print("part 1:", dag8(input))
  print("part 2:",dag8(input, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()