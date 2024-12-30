import sys
import copy

lines = []
for line in sys.stdin:
    lines.append(line)

# Separate the stacks and numbers
stacks = []
numbers = []
found_blank_line = False

for line in lines:
    if line.strip() == "":
        found_blank_line = True
        continue
    if not found_blank_line:
        stacks.append([item.strip() for item in line.strip().split('|')[1:-1]])
    else:
        numbers.append(line.strip().split())
        # Flip the stacks
flipped_stacks = [[] for _ in range(len(stacks[0]))]

for stack in stacks:
    for i, item in enumerate(stack):
        flipped_stacks[i].append(item)



# Initialize arrays for the numbers
array1 = []
array2 = []
array3 = []

# Populate the arrays with the numbers
for number_set in numbers:
    array1.append(int(number_set[0]))
    array2.append(int(number_set[1]))
    array3.append(int(number_set[2]))

# Remove all spaces from flipped_stacks
for stack in flipped_stacks:
    stack[:] = [item for item in stack if item]
# Perform the moves as specified by the arrays
original_flipped_stacks = copy.deepcopy(flipped_stacks)



for move_count, from_stack, to_stack in zip(array1, array2, array3):
    for _ in range(move_count):
        if original_flipped_stacks[from_stack - 1]:  # Check if the from_stack is not empty
            item = original_flipped_stacks[from_stack - 1].pop(0)
            original_flipped_stacks[to_stack - 1].insert(0, item)
        
string = ""
for i in range(len(original_flipped_stacks)):
    string += original_flipped_stacks[i][0]

print("Deel 1: ",string)

for move_count, from_stack, to_stack in zip(array1, array2, array3):
    if len(flipped_stacks[from_stack - 1]) >= move_count:  # Check if there are enough items to move
        items_to_move = flipped_stacks[from_stack - 1][:move_count]
        flipped_stacks[from_stack - 1] = flipped_stacks[from_stack - 1][move_count:]
        flipped_stacks[to_stack - 1] = items_to_move + flipped_stacks[to_stack - 1]

string = ""
for i in range(len(flipped_stacks)):
    string += flipped_stacks[i][0]

print("Deel 2: ",string)