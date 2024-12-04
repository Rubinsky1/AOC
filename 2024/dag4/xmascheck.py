def checkMAS(array, x, y):

    pattern = ['M', 'A', 'S']  # Karaktervolgorde om te vinden
    richtingen = [(-1, 0), (1, 0), (0, -1), (0, 1),  # boven, beneden, links, rechts
                  (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonalen
    totaalgevonden = 0
    for dx, dy in richtingen:  # Loop door alle richtingen
        gevonden = True
        for i in range(len(pattern)):  # Controleer de 3 aangrenzende vakjes
            nx, ny = x + (i + 1) * dx, y + (i + 1) * dy  # Volgende coördinaten
            # Controleer of binnen grenzen
            if nx < 0 or ny < 0 or nx >= len(array) or ny >= len(array[0]):
                gevonden = False
                break
            # Controleer of het karakter overeenkomt
            if array[nx][ny] != pattern[i]:
                gevonden = False
                break
        if gevonden:
            totaalgevonden+=1
    return totaalgevonden
        
def checkXMAS(array, x, y):

    richtingen = [ (-1, -1), (-1, 1), (1, -1), (1, 1)]  # diagonalen
    totaalgevonden = 0
    for dx, dy in richtingen:  # Loop door alle richtingen
        gevonden = False
        nx, ny = x + dx, y +  dy  # Volgende coördinaten
        # Controleer of binnen grenzen
        if nx < 0 or ny < 0 or nx >= len(array) or ny >= len(array[0]) or nx-2*dx < 0 or ny-2*dy < 0 or nx-2*dx >= len(array) or ny-2*dy >= len(array[0])  :
            break
        # Controleer of het karakter overeenkomt
        if array[nx][ny] == 'M':
            if array[nx-2*dx][ny-2*dy] == 'S':
                gevonden = True
    
        if gevonden:
            totaalgevonden+=1
    return totaalgevonden == 2