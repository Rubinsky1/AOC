import sys
import time
from collections import deque
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint

def dag10_read_input(lines):
  lights = []
  buttons = []
  joltages = []
  result = []
  for line in lines:
    line = line.strip().split()
    lights = list(line[0][1:-1])
    buttons = [list(map(int, b.strip('()').split(','))) if b.strip('()') else [] for b in line[1:-1]]
    joltages = list(map(int, line[-1][1:-1].split(',')))
    line = [lights, buttons, joltages]
    result.append(line)
  return result

def dag10(input, part2=False):
  input = dag10_read_input(input)
  answer = 0
  for i in range(len(input)):
    # print("Solving machine", i+1)
    lights, buttons, joltages = input[i]
    
    if not part2:
      initial_state = tuple(lights)
      target = tuple('.' * len(lights))
      
      queue = deque([(initial_state, 0)])
      visited = {initial_state}
      found = False
      
      while queue and not found:
        current_lights, presses = queue.popleft()
        
        for button_idx, button in enumerate(buttons):
          new_lights = list(current_lights)
          for pos in button:
            if 0 <= pos < len(new_lights):
              new_lights[pos] = '#' if new_lights[pos] == '.' else '.'
          
          new_state = tuple(new_lights)
          
          if new_state == target:
            answer += presses + 1
            found = True
            break
          
          if new_state not in visited:
            visited.add(new_state)
            queue.append((new_state, presses + 1))
    
    else:  # part2
      # Use linear algebra approach with Gaussian elimination over GF(2) for part 1
      # For part 2 with joltages, we need to solve a system of linear equations
      
      def build_matrix(buttons, Joltage):
        n = len(Joltage)
        m = len(buttons)
        A = np.zeros((n, m), dtype=int)
        for j, indices in enumerate(buttons):
          for i in indices:
            A[i, j] = 1
        return A
      
      def min_presses(buttons, Joltage):
        A = build_matrix(buttons, Joltage)
        b = np.array(Joltage)
        m = A.shape[1]
        
        c = np.ones(m)  # minimaliseer som(x)
        integrality = np.ones(m, dtype=int)
        bounds = Bounds(np.zeros(m), np.full(m, np.inf))
        constraints = [LinearConstraint(A, b, b)]
        
        res = milp(c=c, integrality=integrality, bounds=bounds, constraints=constraints)
        
        if res.success:
          x = res.x.astype(int)
          total = int(res.fun)
          return total, x.tolist()
        else:
          return None, None
      
      total, button_presses = min_presses(buttons, joltages)
      if total is not None:
        answer += total
      else:
        print(f"No solution found for machine {i+1}")

        
  return answer

def main():
  start_time = time.time()
  filename = sys.argv[1]
  with open(filename, "r") as file:
    lines = file.readlines()
  print("part 1:",dag10(lines))
  print("part 2:",dag10(lines, True))
  print("Execution time: %s seconds" % (time.time() - start_time))

if __name__ == "__main__":
  main()