# Open the file dag2.txt and read its contents
with open('dag2.txt', 'r') as file:
    contents = file.read()

# Split the contents on 'X' and '\n'
split_contents = [line.split('x') for line in contents.split('\n')]

ribbon = 0
wrapping = 0
for line in split_contents:
    # Convert the strings to integers
    l, w, h = map(int, line)
    # Add the total area to the sum
    ribbon += 2*l + 2*w + 2*h - 2*max(l, w, h) + l*w*h
    wrapping += 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

print("deel 1:", wrapping)
print("deel 2:", ribbon)