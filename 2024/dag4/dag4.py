from xmascheck import checkMAS, checkXMAS


with open("dag4.txt", 'r') as file:
    # Elke regel wordt een lijst van karakters
    array = [list(regel.strip()) for regel in file]
totaala = 0
totaalb = 0
for x in range(len(array)):  # Loop door rijen
    for y in range(len(array[0])):  # Loop door kolommen
        if array[x][y] == 'X':  # Startpunt gevonden
            totaala+= checkMAS(array, x, y)  # Controleer alle richtingen
        if array[x][y] == 'A':  # Controleer X-vorm vanaf (x, y)
            totaalb += checkXMAS(array, x, y)
print("totaal aantal XMAS voorkomens is:",totaala)
print("totaal aantal X-MAS voorkomens is:",totaalb)