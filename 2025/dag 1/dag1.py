import sys

def dag1(lines, part2=False):
  rotations = zip(*((line[0], int(line[1:])) for line in lines))
  
  number = 50
  antwoord = 0
  for rotation, count in zip(*rotations):
    delta = 1 if rotation == 'R' else -1
    if part2:
      antwoord += sum(1 for i in range(count) if (number + delta * (i + 1)) % 100 == 0)
    elif number % 100 == 0:
      antwoord += 1
    number += delta * count

  return antwoord

def main():
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag1(lines))
  print("part 2:",dag1(lines, True))

if __name__ == "__main__":
  main()