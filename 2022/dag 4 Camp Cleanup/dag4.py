
def split_lines_in_half(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    first = []
    second = []
    for line in lines:
        line = line.strip().split(',')
        first.append(line[0])
        second.append(line[1])
    
    return first, second

def check_in_range(first, second):
    count = 0
    for i in range(len(first)):
        min_val, max_val = first[i].split('-')
        min_val = int(min_val)
        max_val = int(max_val)
        min_val2, max_val2 = second[i].split('-')
        min_val2 = int(min_val2)
        max_val2 = int(max_val2)
        if (min_val2 <= min_val <= max_val2 and min_val2 <= max_val <= max_val2) or (min_val <= min_val2 <= max_val and min_val <= max_val2 <= max_val):
            count += 1
    
    return count

def check_overlap(first, second):
    count = 0
    for i in range(len(first)):
        min_val, max_val = first[i].split('-')
        min_val = int(min_val)
        max_val = int(max_val)
        min_val2, max_val2 = second[i].split('-')
        min_val2 = int(min_val2)
        max_val2 = int(max_val2)
        if (min_val2 <= min_val <= max_val2 or min_val2 <= max_val <= max_val2) or (min_val <= min_val2 <= max_val or min_val <= max_val2 <= max_val):
            count += 1
    
    return count
file = 'dag4.txt'
first, second = split_lines_in_half(file)
print("deel 1 :",check_in_range(first, second))
print("deel 2 :",check_overlap(first, second))