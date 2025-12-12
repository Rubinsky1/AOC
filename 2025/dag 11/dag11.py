import sys
import time

def dag11walker(cable, position, dac, fft, part2=False, memo=None):
  if memo is None:
    memo = {}
  
  key = (position, dac, fft)
  if key in memo:
    return memo[key]
  
  answer = 0
  if position == 'dac':
    dac = True
  if position == 'fft':
    fft = True
  if position == 'out':
    if not part2:
      return 1
    else:
      if dac and fft:
        return 1
      else:
        return 0
      
  for line in cable:
    if line[0] == position:
      for conn in line[1]:
        answer += dag11walker(cable, conn, dac, fft, part2, memo)
      break
  
  memo[key] = answer
  return answer

def dag11(input, part2=False):
  cable = []
  for line in input:
    line = line.strip().split(':')
    cable.append([line[0], list(line[1].strip().split(' '))])


  if not part2:
    return dag11walker(cable, 'you', False, False)
  if part2:
    return dag11walker(cable, 'svr', False, False, True)
def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag11(lines))
  print("part 2:",dag11(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()