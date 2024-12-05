# Variabelen voor time en distance
time = []
distance = []
tijden = []
aantal = 0
som = 1
# Open het bestand en lees de regels in
with open("dag6.txt", "r") as file:
    for line in file:
        # Verwijder eventuele extra spaties aan het begin en einde van de regel
        line = line.strip()

        if line.startswith("Time"):
            # Verwijder "Time:" en split de rest van de waarden
            time = list(map(int, line.split()[1:]))
        elif line.startswith("Distance"):
            # Verwijder "Distance:" en split de rest van de waarden
            distance = list(map(int, line.split()[1:]))

for race in range(len(time)):
    for i in range(time[race]):
        tijd = (time[race]-i)*i
        if tijd > distance[race]:
            aantal+=1
    som = som*aantal
    aantal = 0
    tijden.clear()

# Print de arrays voor time en distance
print(som)

