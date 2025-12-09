import sys
import time

def dag9(lines, part2=False):
  directions = {'R': (1, 0), 'L': (-1, 0), 'U': (0, 1), 'D': (0, -1)}
  tail_point = (0, 0)
  head_position = (0,0)
  visited_positions = set()
  visited_positions.add(tail_point)
  for line in lines:
    dir, steps = line.strip().split()
    steps = int(steps)
    dx, dy = directions[dir]
    for _ in range(steps):
      head_x, head_y = head_position
      head_x += dx
      head_y += dy
      head_position = (head_x, head_y)
      tail_x, tail_y = tail_point
      if abs(head_x - tail_x) > 1 or abs(head_y - tail_y) > 1:
        if head_x > tail_x:
          tail_x += 1
        elif head_x < tail_x:
          tail_x -= 1
        if head_y > tail_y:
          tail_y += 1
        elif head_y < tail_y:
          tail_y -= 1
        tail_point = (tail_x, tail_y)
        visited_positions.add(tail_point)
  return len(visited_positions)
def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  

  print("part 1:", dag9(lines))
  print("part 2:",dag9(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()