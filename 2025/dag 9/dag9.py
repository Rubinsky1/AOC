import sys
import time

def dag9(lines, part2=False):
  points = [(int(x), int(y)) for x, y in (line.strip().split(',') for line in lines)]
  n = len(points)
  biggest = 0
  hulp = False
  # Precompute bounding boxes reduces time complexity significantly
  if part2:
    bboxes = [(min(points[k][0], points[k+1][0]), 
               max(points[k][0], points[k+1][0]),
               min(points[k][1], points[k+1][1]),
               max(points[k][1], points[k+1][1])) 
              for k in range(n-1)]
  
  for i in range(n):
    xi, yi = points[i]
    for j in range(i + 1, n):  
      xj, yj = points[j]
      area = (abs(xi - xj) + 1) * (abs(yi - yj) + 1)
      
      if area <= biggest:
        continue
        
      if part2:
        # Compute rectangle bounds once
        min_x, max_x = min(xi, xj), max(xi, xj)
        min_y, max_y = min(yi, yj), max(yi, yj)
        
        # Check for overlap with precomputed bboxes
        overlap = any(max_x > bbox_min_x and bbox_max_x > min_x and 
                      max_y > bbox_min_y and bbox_max_y > min_y
                      for bbox_min_x, bbox_max_x, bbox_min_y, bbox_max_y in bboxes)
        
        if not overlap:
          biggest = area
      else:
        biggest = area

  return biggest

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag9(lines))
  print("part 2:",dag9(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()