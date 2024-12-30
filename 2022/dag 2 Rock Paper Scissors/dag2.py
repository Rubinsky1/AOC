# Read the file and parse the values into two arrays
array_a = []
array_b = []

with open('dag2.txt', 'r') as file:
    for line in file:
        a, b = line.split()
        array_a.append(a)
        array_b.append(b)
Sum = 0
for i in range(len(array_a)):
    if (array_a[i] == 'A' and array_b[i] == 'Z') or (array_a[i] == 'B' and array_b[i] == 'X') or (array_a[i] == 'C' and array_b[i] == 'Y'):
        Sum += 0
    elif (array_b[i] == 'X' and array_a[i] == 'C') or (array_b[i] == 'Y' and array_a[i] == 'A') or (array_b[i] == 'Z' and array_a[i] == 'B'):
        Sum += 6
    else:
        Sum += 3
    if array_b[i] == 'X':
        Sum += 1
    elif array_b[i] == 'Y':
        Sum += 2
    elif array_b[i] == 'Z':
        Sum += 3

print("Total score deel 1:", Sum)

Sum = 0
for i in range(len(array_a)):
    if (array_b[i] == 'X'):
        Sum += 0
    elif (array_b[i] == 'Z'):
        Sum += 6
    else:
        Sum += 3
    if array_b[i] == 'Z':  # We need to win against array_a[i]
        if array_a[i] == 'A':
            Sum += 2  # B wins against A
        elif array_a[i] == 'B':
            Sum += 3  # C wins against B
        elif array_a[i] == 'C':
            Sum += 1  # A wins against C
    elif array_b[i] == 'Y':  # We need to tie with array_a[i]
        if array_a[i] == 'A':
            Sum += 1  # A ties with A
        elif array_a[i] == 'B':
            Sum += 2  # B ties with B
        elif array_a[i] == 'C':
            Sum += 3  # C ties with C
    elif array_b[i] == 'X':  # We need to lose against array_a[i]
        if array_a[i] == 'A':
            Sum += 3  # C loses to A
        elif array_a[i] == 'B':
            Sum += 1  # A loses to B
        elif array_a[i] == 'C':
            Sum += 2  # B loses to C

print("Total score deel 2:", Sum)