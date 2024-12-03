import sys

totaal = 0  # Variabele voor het totaal

# Lees regels van stdin
for line in sys.stdin:
    getallen = line.strip().split() 
    totaal += int(getallen[0]) * int(getallen[1])

# Print het totaal
print("Het totaal is:", totaal)
