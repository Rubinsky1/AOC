import time
import sys

def count_char_in_columns(grid, char):
  if not grid:
    return []
  rows = len(grid)
  cols = len(grid[0])
  counts = [0] * cols
  for r in range(rows):
    for c in range(cols):
      if grid[r][c] == char:
        counts[c] += 1
  return counts

def dag25_read_input(lines):
  keys = []
  locks = []
  current_block = []
  lock = False
  for line in lines:
    line = line.strip()
    if line == "":
      if current_block:
        if all(c == '#' for c in current_block[0]):
          lock = True
      if current_block and lock:
        locks.append(count_char_in_columns(current_block, '#'))
        current_block = []
      if current_block and not lock:
        keys.append(count_char_in_columns(current_block, '#'))
        current_block = []
      lock = False
    else:
      current_block.append(line)
  
  if current_block:
    keys.append(count_char_in_columns(current_block, '#'))
  
  return keys, locks

def dag25(lines, part2=False):
  keys, locks = dag25_read_input(lines)
  fitting = True
  answer = 0
  for key in keys:
    for lock in locks:
      for i in range(len(lock)):
        if key[i] + lock[i] > 7:
          fitting = False
          
      if fitting:
        answer += 1
      fitting = True  
  return answer

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag25(lines))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()