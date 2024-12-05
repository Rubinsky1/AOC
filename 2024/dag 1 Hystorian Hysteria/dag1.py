# Bestand openen en uitlezen
with open("test.txt", "r") as file:
    # Lees elke regel en splits op basis van whitespace
    lines = file.readlines()

# Twee lege arrays om de waarden te bewaren
array_left = []
array_right = []

# Elke regel verwerken
for line in lines:
    # Verwijder witruimte en splits op spatie/tab
    values = line.strip().split()
    # Toevoegen aan respectievelijke arrays
    array_left.append(int(values[0]))
    array_right.append(int(values[1]))

# Arrays sorteren
sorted_left = sorted(array_left)
sorted_right = sorted(array_right)

# Bereken de totale afstand
total_distance = 0
for i in range(len(sorted_left)):
    # Bereken de afstand tussen de waarden
    distance = abs(sorted_left[i] - sorted_right[i])
    total_distance += distance

print("totale afstand :",total_distance)

# Frequentietabel voor de rechter lijst opbouwen
right_counts = {}
for num in array_right:
    if num in right_counts:
        right_counts[num] += 1
    else:
        right_counts[num] = 1

# Bereken de totale gelijkenisscore
similarity_score = 0
for num in array_left:
    # Kijk of het getal voorkomt in de rechter lijst
    frequency = right_counts[num] if num in right_counts else 0
    # Tel bij de score op: getal * frequentie
    similarity_score += num * frequency

# Print de uiteindelijke gelijkenisscore
print("Gelijkenisscore tussen de lijsten:", similarity_score)