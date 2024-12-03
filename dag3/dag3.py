import sys

totaal = 0  # Variabele voor het totaal

# Lees regels van stdin
for line in sys.stdin:
    # Splits de lijn op spatie om de twee getallen te verkrijgen
    getallen = line.strip().split()
    if len(getallen) == 2:  # Zorg ervoor dat er precies twee getallen zijn
        # Haal de twee getallen op en converteer ze naar integers
        eerste_getal = int(getallen[0])
        tweede_getal = int(getallen[1])
        
        # Vermenigvuldig de getallen en voeg het product toe aan het totaal
        totaal += eerste_getal * tweede_getal

# Print het totaal
print("Het totaal is:", totaal)
