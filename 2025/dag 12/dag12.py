import sys
import time

def dag12_read_input(lines):
  tiles = []
  field = []
  tile = []
  for line in lines:
    line = line.strip().split('\n')
    for row in line:
      tile.append(list(row))
    tiles.append(tile[1:])
    leftover = tile[0]
    tile = []
  field.append(''.join(leftover))
  for tile in tiles[-1]:
    field.append(''.join(tile))
  fields = []
  for field_line in field:
    field_line = field_line.strip().split(':')
    size = list(map(int, field_line[0].strip().split('x')))
    stones = list(map(int, field_line[1].strip().split(' ')))
    fields.append([size, stones])
  return tiles[:-1], fields

def dag12(input):
  answer = 0
  answer2 = 0
  tiles, fields = dag12_read_input(input)
  for field in fields:
    size, stones = field
    truesize = size[0] * size[1]
    sumofstones = sum(stones)*9
    if truesize >= sumofstones:
      answer +=1
    else:
      sumofstones = 0
      for i, stone in enumerate(stones):
        sumofstones += stone*sum(row.count('#') for row in tiles[i])
        
      if truesize < sumofstones:
        answer2 +=1

  return answer

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.read().split('\n\n')
  print("part 1:",dag12(lines))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()