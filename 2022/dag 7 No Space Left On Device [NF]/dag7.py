with open('dag7.txt', 'r') as file:
    content = file.read()
    print(content)

    lines = content.split('\n')
    array = []
    current_array = []

    for line in lines:
        if line.startswith('$ ls'):
            current_array = []
            array.append(current_array)
        elif line.startswith('$'):
            continue
        else:
            current_array.append(line)

    print(array)