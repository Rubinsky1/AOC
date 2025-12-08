import sys
import time

def dag7(lines, part2=False):
  ans = 0
  splitters = ([[1 if char == '^' else 2 if char == 'S' else 0 for char in line.strip()] for line in lines])
  rows = len(splitters)
  cols = len(splitters[0])
  for i in range(rows - 1):
    for j in range(cols):
      if splitters[i][j] >= 2 and splitters[i+1][j] != 1:
        splitters[i+1][j] += splitters[i][j] 
      elif splitters[i][j] >= 2 and splitters[i+1][j] == 1:
        splitters[i+1][j+1]+= splitters[i][j]
        splitters[i+1][j-1]+= splitters[i][j]
        if not part2:
          ans +=1
  if part2:
    for col in range(cols):
      if splitters[rows-1][col] >= 2:
        ans += int(splitters[rows-1][col]/2) 
  return ans

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag7(lines))
  print("part 2:",dag7(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()