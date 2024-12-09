from dag6funct import read_2d_array, find_coordinates, binnen
einde = False
parkour = read_2d_array("dag6.txt")
# Simulatie van de bewegingen van de bewaker
while not einde:
    # Vind de huidige positie en richting van de bewaker
    x, y = find_coordinates(parkour, ["^", "<", ">", "v"])
    current_dir = parkour[x][y]
    parkour[x][y] = "X"  # Markeer huidige positie als bezocht
    if current_dir == "^":
        if not binnen(x - 1, y, parkour) :
            einde = True
        elif parkour[x - 1][y] == "#":
            parkour[x][y] = ">"
        else:
            parkour[x - 1][y] = "^"
    elif current_dir == ">":
        if not binnen(x, y + 1, parkour):
            einde = True
        elif parkour[x][y + 1] == "#":
            parkour[x][y] = "v"
        else:
            parkour[x][y + 1] = ">"
    elif current_dir == "v":
        if not binnen(x + 1, y, parkour):
            einde = True
        elif parkour[x + 1][y] == "#":
            parkour[x][y] = "<"
        else:
            parkour[x + 1][y] = "v"
    elif current_dir == "<":
        if not binnen(x, y - 1, parkour) :
            einde = True
        elif parkour[x][y - 1] == "#":
            parkour[x][y] = "^"
        else:
            parkour[x][y - 1] = "<"


# Print het eindresultaat
print(sum(row.count('X') for row in parkour))