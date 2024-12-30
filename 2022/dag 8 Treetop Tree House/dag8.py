def lees_bestand_naar_2d_array(bestandsnaam):
    with open(bestandsnaam, 'r') as bestand:
        lijnen = bestand.readlines()
        array_2d = [[int(cijfer) for cijfer in lijn.strip()] for lijn in lijnen]
    
    return array_2d

def check_hoger_in_route(array_2d):
    boolean_array = [[False for _ in rij] for rij in array_2d]
    rijen = len(array_2d)
    kolommen = len(array_2d[0])

    for i in range(rijen):
        max_links = max_rechts = -1
        for j in range(kolommen):
            if array_2d[i][j] > max_links:
                max_links = array_2d[i][j]
                boolean_array[i][j] = True
            if array_2d[i][kolommen - j - 1] > max_rechts:
                max_rechts = array_2d[i][kolommen - j - 1]
                boolean_array[i][kolommen - j - 1] = True

    for j in range(kolommen):
        max_boven = max_beneden = -1
        for i in range(rijen):
            if array_2d[i][j] > max_boven:
                max_boven = array_2d[i][j]
                boolean_array[i][j] = True
            if array_2d[rijen - i - 1][j] > max_beneden:
                max_beneden = array_2d[rijen - i - 1][j]
                boolean_array[rijen - i - 1][j] = True
    aantal_true = sum(sum(rij) for rij in boolean_array)
    return aantal_true


def vermenigvuldig_bomen(array_2d):
    rijen = len(array_2d)
    kolommen = len(array_2d[0])
    max_product = 0

    for i in range(rijen):
        for j in range(kolommen):
            links = rechts = boven = beneden = 0

            # Tel bomen naar links
            for k in range(j - 1, -1, -1):
                links += 1
                if array_2d[i][k] >= array_2d[i][j]:
                    break

            # Tel bomen naar rechts
            for k in range(j + 1, kolommen):
                rechts += 1
                if array_2d[i][k] >= array_2d[i][j]:
                    break

            # Tel bomen naar boven
            for k in range(i - 1, -1, -1):
                boven += 1
                if array_2d[k][j] >= array_2d[i][j]:
                    break

            # Tel bomen naar beneden
            for k in range(i + 1, rijen):
                beneden += 1
                if array_2d[k][j] >= array_2d[i][j]:
                    break

            product = links * rechts * boven * beneden
            if product > max_product:
                max_product = product

    return max_product



bestandsnaam = 'dag8.txt'
array_2d = lees_bestand_naar_2d_array(bestandsnaam)
print("deel 1:", check_hoger_in_route(array_2d))
print("deel 2:",vermenigvuldig_bomen(array_2d))