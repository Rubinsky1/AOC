# Bestand inlezen
with open("dag4.txt", "r") as file:
    lines = file.readlines()

total_points = 0  # Totale punten
card_points = []  # Punten per kaart

for line in lines:
    # Splits op "|"
    parts = line.split("|")
    if len(parts) != 2:
        continue  # Overslaan als de lijn niet het juiste formaat heeft
    
    # Winning numbers en jouw nummers
    winning_numbers = list(map(int, parts[0].split()[2:]))  # Na "Card X:"
    your_numbers = list(map(int, parts[1].split()))

    # Bepaal overeenkomende nummers
    matches = set(winning_numbers).intersection(your_numbers)
    match_count = len(matches)

    # Bereken punten
    if match_count > 0:
        points = 1 * (2 ** (match_count - 1))  # 1 punt voor de eerste match, dan verdubbelen
        card_points.append(points)
        total_points += points
    else:
        card_points.append(0)

# Print de resultaten
for i, points in enumerate(card_points, start=1):
    print(f"Card {i} is worth {points} points.")
print(f"Total points: {total_points}")
