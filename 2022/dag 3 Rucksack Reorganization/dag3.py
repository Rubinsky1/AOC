def split_lines_in_half(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    first_half = []
    second_half = []

    for line in lines:
        line = line.strip()
        mid_index = len(line) // 2
        first_half.append(line[:mid_index])
        second_half.append(line[mid_index:])

    return first_half, second_half

# Example usage
file_path = 'dag3.txt'
first_half, second_half = split_lines_in_half(file_path)
som = 0
for i in range(len(first_half)):
    common_letters = set(first_half[i]).intersection(second_half[i])
    for i in common_letters:
        if i.islower():
            som += ord(i) - ord('a') + 1
        elif i.isupper():
            som += ord(i) - ord('A') + 27
print("Deel 1: ", som)
som = 0
with open(file_path, 'r') as file:
    lines = file.readlines()

for i in range(0, len(lines), 3):
    group = lines[i:i+3]
    if len(group) < 3:
        continue
    group = [line.strip() for line in group]
    common_letters = set(group[0]).intersection(group[1]).intersection(group[2])
    for letter in common_letters:
        if letter.islower():
            som += ord(letter) - ord('a') + 1
        elif letter.isupper():
            som += ord(letter) - ord('A') + 27

print("Deel 2: ", som)
