def read_2d_array(filename):
    with open(filename, 'r') as file:
    # Elke regel wordt een lijst van karakters
        array = [list(regel.strip()) for regel in file]
    
    return array

def find_coordinates(array, target):
    for row_index, row in enumerate(array):
        for col_index, value in enumerate(row):
            if value in target:
                return (row_index, col_index)
    return None  # Geen match gevonden

def binnen(x, y, array):
    # Controleer of x en y binnen de geldige grenzen liggen
    if x < 0 or y < 0 or x >= len(array) or y >= len(array[0]):
        return False
    return True
