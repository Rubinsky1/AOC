from collections import Counter

def replace_j(hand):
    # Als er 5 'J's zijn, vervang ze allemaal door 'A'
    if hand.count('J') == 5:
        return hand.replace('J', 'A')

    # Tel de frequentie van elk karakter in de string
    count = Counter(hand)

    # Vind het meest voorkomende karakter, behalve 'J'
    if 'J' in count:
        del count['J']  # Verwijder 'J' uit de tellingen
    most_common = count.most_common(1)[0][0]  # Het meest voorkomende karakter

    # Vervang alle 'J's door het meest voorkomende karakter
    hand = hand.replace('J', most_common)
    
    return hand



def sort(array1, array2):
    card_order = {'A': 12, 'K': 11, 'Q': 10, 'J': 9, 'T': 8, '9': 7, '8': 6, '7': 5, '6': 4, '5': 3, '4': 2, '3': 1, '2': 0}
    result = []  # Hier slaan we de frequentie-arrays op

    for i in range(len(array1)):
        hand = array1[i]
        count = Counter(hand)
        frequencies = list(count.values())
        frequencies.sort(reverse=True)  # Sorteer van groot naar klein
        result.append((hand, frequencies, array2[i]))  # Voeg de hand, frequenties en de corresponderende waarde uit array2 toe als tuple

    # Sorteer eerst op de frequenties (met een secundaire sortering op kaartvolgorde)
    result.sort(key=lambda x: (x[1], [card_order[card] for card in x[0]]))

    # Retourneer de handen en de bijbehorende waarden uit array2 in de juiste volgorde
    sorted_bids = [bid for _, _, bid in result]  # Gebruik `bid` in plaats van `i`

    totaal = 0
    for i in range(len(sorted_bids)):
        totaal += (i+1)*sorted_bids[i]
    return totaal

def sort2(array1, array2):
    card_order = {'A': 12, 'K': 11, 'Q': 10, 'J': 0, 'T': 9, '9': 8, '8': 7, '7': 6, '6': 5, '5': 4, '4': 3, '3': 2, '2': 1}
    result = []  # Hier slaan we de frequentie-arrays op

    for i in range(len(array1)):
        hand = array1[i]
        count = Counter(replace_j(hand))
        frequencies = list(count.values())
        frequencies.sort(reverse=True)  # Sorteer van groot naar klein
        result.append((array1[i], frequencies, array2[i]))  # Voeg de hand, frequenties en de corresponderende waarde uit array2 toe als tuple

    # Sorteer eerst op de frequenties (met een secundaire sortering op kaartvolgorde)
    result.sort(key=lambda x: (x[1], [card_order[card] for card in x[0]]))

    sorted_bids = [bid for _, _, bid in result]  # Gebruik `bid` in plaats van `i`

    totaal = 0
    for i in range(len(sorted_bids)):
        totaal += (i+1)*sorted_bids[i]
    return totaal



def readfile_2_array(infile):
    links = []
    rechts = []
    with open(infile, "r") as file:
        lines = file.readlines()

    # Elke regel verwerken
    for line in lines:
        # Verwijder witruimte en splits op spatie/tab
        values = line.strip().split()
        # Voeg de waarden toe aan de respectievelijke arrays
        links.append(values[0])
        rechts.append(int(values[1]))
    return links, rechts