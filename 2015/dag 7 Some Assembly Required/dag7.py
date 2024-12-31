# Open the file in read mode
with open('dag7.txt', 'r') as file:
    # Read the file line by line
    lines = file.readlines()

# Print each line
for line in lines:
    print(line.strip())