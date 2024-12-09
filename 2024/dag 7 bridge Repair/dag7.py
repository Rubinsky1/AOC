from dag7funct import calibrations

# Inlezen van de bestand
with open("dag7.txt", "r") as file:
    lines = file.readlines()

total_calibration = calibrations(lines, 0)

# Output de som van de testwaarden die waar zijn
print(f"Totale calibratiewaarde: {total_calibration}")
total_calibration2 = calibrations(lines, 1)
print(f"Totale calibratiewaarde: {total_calibration2}")