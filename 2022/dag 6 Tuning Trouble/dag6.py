# Open the file dag6.txt and read its content into a string
with open('dag6.txt', 'r') as file:
    content = file.read()

for i in range(len(content)):
    if i > 4 and len(set(content[i-4:i])) == 4:
        print("deel2: ",i)
        break

for i in range(len(content)):
    if i > 14 and len(set(content[i-14:i])) == 14:
        print("deel2: ",i)
        break