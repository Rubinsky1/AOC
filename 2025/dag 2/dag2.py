def check_repetition(num_str):
  length = len(num_str)
  for i in range(1, length // 2 + 1):
    if length % i == 0:
      substring = num_str[:i]
      repetitions = length // i
      if substring * repetitions == num_str:
        return num_str
  return 0

def check_single_repetition(num_str):
  length = len(str(num_str))
  if length % 2 == 0:
    mid = length // 2
    first_half = str(num_str)[:mid]
    second_half = str(num_str)[mid:]
    if first_half == second_half:
      return num_str
  return 0

def numRepetitions(lines, partA = True):
  count = 0
  IdList = lines[0].strip().split(",")
  for i in range(len(IdList)):
      j = IdList[i].strip().split("-")
      start, end = map(int, j)
      for k in range(start, end + 1):
        if partA:
          count += int(check_single_repetition(str(k)))
        else:
          count += int(check_repetition(str(k)))
  return count


with open("dag2.txt", "r") as file:
  # Lees elke regel en splits op basis van whitespace
  lines = file.readlines()
   
print("Part A:", numRepetitions(lines))
print("Part B:", numRepetitions(lines, partA=False))