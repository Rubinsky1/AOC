from dag9funct import extrapoluted, extrapoluted_back
# Bestand openen en uitlezen
with open("dag9.txt", "r") as file:
    lines = file.readlines()
    

print("deel 1:", extrapoluted(lines))
print("deel 2:", extrapoluted_back(lines))

