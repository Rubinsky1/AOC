import sys
import time

def largest_Xnumber(lines, ammount=12):
  sum = 0
  all = {}
  bigest = {}
  for line in lines:
    bigest = {}
    for pos, number in enumerate(line):
      all[pos] = number
    for i in range(ammount):
      max_bigest_pos = max(bigest.keys()) if bigest else -1
      valid_positions = {pos: val for pos, val in all.items() if pos < len(line) -(ammount - i) and pos > max_bigest_pos}
      max_pos = min(pos for pos, val in valid_positions.items() if val == max(valid_positions.values()))
      bigest[max_pos] = all[max_pos]
      del all[max_pos]
    combined = ''.join([bigest[key] for key in sorted(bigest.keys())])
    sum += int(combined)
  return sum

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",largest_Xnumber(lines, ammount=2))
  print("part 2:",largest_Xnumber(lines, ammount=12))
  print("Execution time: %s seconds" % (time.time() - start_time))
  
if __name__ == "__main__":
  main()