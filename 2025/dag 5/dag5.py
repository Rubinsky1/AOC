import sys
import time

def dag5_read(lines):
  id_ranges = []
  available_ids = []
  parsing_ranges = True
  
  for line in lines:
    line = line.strip()
    if line == "":
      parsing_ranges = False
      continue
    
    if parsing_ranges:
      id_ranges.append(line)
    else:
      available_ids.append(line)
  
  return id_ranges, available_ids

def dag5(input, part2=False):
  result = 0
  id_ranges, available_ids = input
  if not part2:
    for id in available_ids:
      for id_range in id_ranges:
        start, end = id_range.split("-")
        if int(start) <= int(id) <= int(end):
          result += 1
          break
  else:
    sorted_ranges = (sorted(id_ranges, key=lambda x: int(x.split("-")[0])))
    stored = 0
    for range in sorted_ranges:
      start, end = map(int, range.split("-"))
      if start <= stored:
        start = stored + 1
      if start <= end:
        result += (end - start + 1)
        stored = end
  return result

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  input = dag5_read(lines)
  print("part 1:",dag5(input))
  print("part 2:",dag5(input, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()