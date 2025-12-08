import sys
import time

def dag4(paperGrid, part2=False):
  
  rows = len(paperGrid)
  cols = len(paperGrid[0]) 
  total = 0
  for i in range(rows):
    for j in range(cols):
      if paperGrid[i][j] == 1:
        neighbours = 0
        # Check all 8 neighbors
        for di in [-1, 0, 1]:
          for dj in [-1, 0, 1]:
            if di == 0 and dj == 0:
              continue
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < cols:
              if paperGrid[ni][nj] == 1:
                neighbours += 1
        if neighbours <= 3:
          total += 1
          if part2:
            paperGrid[i][j] = 0
  if part2:
    if total == 0:
      return total
    else:
      return total + dag4(paperGrid, part2)
  return total


def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  paperGrid = ([[1 if char == '@' else 0 for char in line.strip()] for line in lines])
  print("part 1:",dag4(paperGrid))
  print("part 2:",dag4(paperGrid, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()