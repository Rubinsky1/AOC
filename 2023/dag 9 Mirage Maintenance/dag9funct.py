
def extrapoluted(lines):
        
    array = []
    lower = []
    gaan = True
    totaal = 0
    # Elke regel verwerken
    for line in lines:
        array.clear()
        values = list(map(int, line.strip().split()))
        array.append(values)  # Voeg de huidige regel toe aan array
        counter = 0
        while gaan:
            lower.clear()  # Reset de lower lijst elke keer

            # Gebruik de waarden van de huidige regel (array[counter])
            for i in range(len(array[counter]) - 1):
                lower.append(array[counter][i+1] - array[counter][i ])  # Bereken het verschil

            array.append(lower[:])  # Voeg de lower lijst toe aan array

            counter += 1
            if all(x == 0 for x in lower):
                gaan = False  # Stop de while-lus als alle waarden 0 zijn
        gaan = True
        toevoegen = 0
        for i in range(len(array)-1, -1, -1):
            array[i].append(toevoegen)
            toevoegen = array[i][-1]+array[i-1][-1]
        totaal +=toevoegen
    return totaal

def extrapoluted_back(lines):
        
    array = []
    lower = []
    gaan = True
    totaal = 0
    # Elke regel verwerken
    for line in lines:
        array.clear()
        values = list(map(int, line.strip().split()))
        array.append(values)  # Voeg de huidige regel toe aan array
        counter = 0
        while gaan:
            lower.clear()  # Reset de lower lijst elke keer

            # Gebruik de waarden van de huidige regel (array[counter])
            for i in range(len(array[counter]) - 1):
                lower.append(array[counter][i+1] - array[counter][i ])  # Bereken het verschil

            array.append(lower[:])  # Voeg de lower lijst toe aan array

            counter += 1
            if all(x == 0 for x in lower):
                gaan = False  # Stop de while-lus als alle waarden 0 zijn
        gaan = True
        toevoegen = 0
        for i in range(len(array)-1, -1, -1):
            array[i].insert(0, toevoegen)
            toevoegen = array[i-1][0]-array[i][0]
        totaal -=toevoegen
    return totaal