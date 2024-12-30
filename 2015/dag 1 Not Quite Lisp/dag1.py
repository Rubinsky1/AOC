# Open the file 'dag1.txt' and read its content
with open('dag1.txt', 'r') as file:
    content = file.read()
counter = 0
position = []
# Print the content of the file
for i in range(len(content)):
    if content[i] == '(':
        counter += 1
    elif content[i] == ')':
        counter -= 1
    if counter < 0 :
        position.append(i+1)


print("deel 1:",counter)
print("deel 2:", position[0])