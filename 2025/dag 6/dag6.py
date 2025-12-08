import sys
import time

def dag6_read_part1(lines):
  array = []
  nicer = []
  sum = []
  for line in lines:
    line = line.strip()
    numbers = [x for x in line.split()]
    array.append(numbers)
  
  rows = len(array)
  cols = len(array[0])
  for i in range(cols):
    for j in range(rows-1, -1, -1):
      if array[j][i].strip() != "":
        sum.append(array[j][i])
    nicer.append(sum.copy())
    sum.clear()
  return nicer


def dag6_read_part2(lines):
  array = []
  sum = []
  rows = len(lines)
  cols = len(lines[0])
  ans = ""
  for col in range(cols):
    ans = ""

    if lines[rows-1][col].strip() != "":
      sum.append(lines[rows-1][col])

    for row in range(rows-1):
      ans += lines[row][col]
    if ans.strip() == "":
      array.append(sum.copy())
      sum.clear()
    else:
      sum.append(ans.strip())

  return array

def dag6(lines, part2=False):
  input = dag6_read_part2(lines) if part2 else dag6_read_part1(lines)
  answer = 0
  part_sum = 0
  mult = 1
  for sum in input:
    for part in sum[1:]:
      mult *= int(part)
      part_sum += int(part)
    if sum[0].strip() == '*':
      answer +=  mult
      mult = 1
      part_sum = 0
    elif sum[0].strip() == '+':
      answer += part_sum 
      part_sum = 0
      mult = 1

        

  return answer

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag6(lines))
  print("part 2:",dag6(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()