import sys
import time

def read_dag24_input(lines):

  values = {}
  wires, gates = lines[0].splitlines(), lines[1].splitlines()
  for line in wires:
    parts = line.strip().split(': ')
    wire_id = parts[0]
    path = parts[1]
    values[wire_id] = int(path)  
  print(values)
  return 0

def dag24(lines, part2=False):
  read_dag24_input(lines)
  return 0

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.read().split("\n\n")
  print("part 1:",dag24(lines))
  print("part 2:",dag24(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()