# Lees het bestand 'dag 13.txt' in
WIDTH = 101
HEIGHT = 103

with open("dag14.txt", "r") as file:
    lines = file.readlines()

# Arrays voor posities en snelheden
positions = []
velocities = []

# Verwerk iedere regel in het bestand
for line in lines:
    line = line.strip()  # Verwijder overtollige spaties of newline karakters
    if not line:  # Sla lege regels over
        continue

    # Deel de lijn op in posities (p) en snelheden (v)
    parts = line.split()
    p_values = parts[0][2:].split(",")  # Verwijder "p=" en splits op ","
    v_values = parts[1][2:].split(",")  # Verwijder "v=" en splits op ","

    # Zet strings om naar integers en voeg toe aan de lijsten
    positions.append([int(p_values[0]), int(p_values[1])])
    velocities.append([int(v_values[0]), int(v_values[1])])

for step in range(100):
    # Tel velocity op bij positions
    for i in range(len(positions)):
        positions[i][0] += velocities[i][0]  # Update x-coördinaat
        positions[i][1] += velocities[i][1]  # Update y-coördinaat

    # Debug-output na elke stap (optioneel)
        positions[i][0] %= WIDTH  # Zorg ervoor dat x binnen [0, WIDTH-1] blijft
        positions[i][1] %= HEIGHT  # Zorg ervoor dat y binnen [0, HEIGHT-1] blijft

# Tellen van posities in elk kwadrant
quadrant_counts = [0, 0, 0, 0]

for x, y in positions:
    # Negeer posities op scheidingslijnen
    if x == WIDTH // 2 or y == HEIGHT // 2:
        continue

    # Bepaal het kwadrant
    if x < WIDTH // 2 and y < HEIGHT // 2:  # Linksboven
        quadrant_counts[0] += 1
    elif x > WIDTH // 2 and y < HEIGHT // 2:  # Rechtsboven
        quadrant_counts[1] += 1
    elif x < WIDTH // 2 and y > HEIGHT // 2:  # Linksonder
        quadrant_counts[2] += 1
    elif x > WIDTH // 2 and y > HEIGHT // 2:  # Rechtsonder
        quadrant_counts[3] += 1

# Vermenigvuldig de aantallen in de kwadranten
result = 1
for count in quadrant_counts:
    result *= count

# Resultaten weergeven
print("Aantal punten per kwadrant:", quadrant_counts)
print("Resultaat van vermenigvuldiging:", result)
