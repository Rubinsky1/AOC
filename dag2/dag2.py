from safe import *

# Bestand openen en uitlezen
with open("test.txt", "r") as file:
    lines = file.readlines()
aantal = 0  # Teller voor veilige rapporten

# Elke regel verwerken
for line in lines:
    values = list(map(int, line.strip().split()))
    
    # Controleer of de oorspronkelijke lijst veilig is
    if is_safe(values):
        aantal += 1
        continue

    # Probeer elk niveau te verwijderen en controleer veiligheid
    veilig = False
    for i in range(len(values)):
        nieuwe_values = values[:i] + values[i+1:]  # Verwijder niveau i
        if is_safe(nieuwe_values):
            veilig = True
            break

    # Als veilig na verwijderen, verhoog de teller
    if veilig:
        aantal += 1

print("Aantal veilige rapporten is:", aantal)
