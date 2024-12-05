# Arrays voor links en rechts
links = []
rechts = []

# Lijst voor de overige regels
overige = []
totaals = 0
totaalg = 0
# Bestand lezen
with open("dag5.txt", "r") as file:
    lines = file.read().strip().split("\n\n")  # Split op de lege regel

# Eerste deel (links en rechts)
eerste_deel = lines[0].strip().split("\n")
for regel in eerste_deel:
    link, recht = map(int, regel.split("|"))
    links.append(link)
    rechts.append(recht)

# Tweede deel (overige lijnen)
tweede_deel = lines[1].strip().split("\n")
for regel in tweede_deel:
    overige.append(list(map(int, regel.split(","))))

for rij in overige:
    check = True
    for i in range(len(links)):
        if links[i] in rij and rechts[i] in rij:
            index_links = rij.index(links[i])
            index_rechts = rij.index(rechts[i])
            # Controleer of de volgorde verkeerd is
            if index_rechts < index_links:
                check = False
    if(check):
        totaalg += rij[len(rij) // 2]

for rij in overige:
    check = False
    while(not check):
        check = True
        for i in range(len(links)):
            if links[i] in rij and rechts[i] in rij:
                index_links = rij.index(links[i]) 
                index_rechts = rij.index(rechts[i])
                if index_rechts < index_links:
                    check = False
                    rij.pop(index_links)  # Verwijder links[i] uit de huidige positie
                    new_index = rij.index(rechts[i])  # Zoek de nieuwe index van rechts[i]
                    rij.insert(new_index, links[i])
    
    totaals += rij[len(rij) // 2]
    totaal = totaals - totaalg
# Resultaten printen
print("totaal:", totaal)

