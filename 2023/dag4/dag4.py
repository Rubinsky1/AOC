# Bestanden inlezen
with open("dag4.txt", "r") as file:
    lines = file.readlines()

# Verwerk de kaarten
cards = []
for line in lines:
    parts = line.split("|")
    if len(parts) != 2:
        continue  # Overslaan als de lijn niet het juiste formaat heeft
    winning_numbers = list(map(int, parts[0].split()[2:]))  # Na "Card X:"
    your_numbers = list(map(int, parts[1].split()))
    cards.append((winning_numbers, your_numbers))

# Functie om te bepalen hoeveel overeenkomsten er zijn
def get_match_count(winning_numbers, your_numbers):
    return len(set(winning_numbers).intersection(your_numbers))

# Initialiseer een lijst van kaarten die we gaan scoren
cards_to_process = list(range(len(cards)))  # Begin met alle kaarten
processed = set()  # Hou bij welke kaarten al verwerkt zijn
card_win_count = [0] * len(cards)  # Aantal keren dat elke kaart is "gewonnen"
total_matches = 0

while cards_to_process:
    current_card_index = cards_to_process.pop()
    if current_card_index in processed:
        continue  # Deze kaart is al verwerkt

    # Markeer de kaart als verwerkt
    processed.add(current_card_index)

    # Haal de kaart informatie op
    winning_numbers, your_numbers = cards[current_card_index]
    match_count = get_match_count(winning_numbers, your_numbers)

    # Voeg de aantal overeenkomsten toe aan het totaal
    total_matches += match_count

    # Als er overeenkomsten zijn, winnen we nieuwe kaarten
    if match_count > 0:
        # Voeg de volgende kaarten toe aan de te verwerken kaarten
        for i in range(current_card_index + 1, current_card_index + match_count + 1):
            if i < len(cards):
                cards_to_process.append(i)

# Print het resultaat
print(f"Total matches: {total_matches}")
