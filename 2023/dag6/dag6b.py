# Variabelen voor time en distance

aantal = 0
with open("dag6.txt", "r") as file:
    for line in file:
        # Verwijder extra spaties en tekst, en lees het getal als één geheel
        line = line.strip().replace(" ", "")  
        if line.startswith("Time"):
            time = int(line.split(":")[1])
        elif line.startswith("Distance"):
            distance = int(line.split(":")[1])

for i in range(time):
    tijd = (time-i)*i
    if tijd > distance:
        aantal+=1


print(aantal)
