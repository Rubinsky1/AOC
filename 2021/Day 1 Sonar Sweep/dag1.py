def count_higher(input):
  count = 0
  for i in range(1, len(input)):
    if input[i] > input[i-1]:
      count += 1

  return count

def count_3_higher(input):
  count = 0
  for i in range(1, len(input)-2):
    
    A = sum(input[i-1:i+2]) / 3
    B = sum(input[i:i+3]) / 3
    if B > A:
      count += 1
  return count

def read_input(file):
  with open(file) as f:
    return [int(x) for x in f.read().splitlines()]
  
file = "dag1.txt"
input = read_input(file)
print("deel 1:", count_higher(input))
print("deel 2:", count_3_higher(input))