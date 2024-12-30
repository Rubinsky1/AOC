with open("dag1.txt", "r") as file:
    # Lees elke regel en splits op basis van whitespace
    lines = file.readlines()

# Twee lege arrays om de waarden te bewaren
array = []
sum = 0
# Elke regel verwerken
for line in lines:
    if line != "\n":
        sum += int(line)
    else:
        array.append(sum)
        sum = 0

print("deel 1:", max(array))
sum = 0
for _ in range(3):
    sum += max(array)
    array.remove(max(array))

print("deel 2:", sum)