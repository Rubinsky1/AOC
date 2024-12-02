def is_safe(values):
    stijgend = False
    dalend = False
    
    #bepaal of deze line stijgend of dalend zou moeten zijn
    verschil = values[1] - values[0]
    if 0 < verschil <= 3:
        stijgend = True
    elif -3 <= verschil < 0:
        dalend = True
    else:
        return False

    # Controleer de resterende paren
    for i in range(len(values) - 1):
        verschil = values[i + 1] - values[i]
        if stijgend:
            if not (0 < verschil <= 3):
                return False
        elif dalend:
            if not (-3 <= verschil < 0):
                return False

    return True