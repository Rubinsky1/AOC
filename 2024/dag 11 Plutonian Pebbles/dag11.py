import subprocess
import matplotlib.pyplot as plt

# Functie om het C++-programma aan te roepen en de uitvoer te lezen
def run_cpp_program(loops):
    # Aanroep van het C++-programma met 'loops' als argument
    result = subprocess.run(['./main', str(loops)], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Haal de uitvoer op
    output = result.stdout
    return output


# Lijst om de resultaten op te slaan
loops_range = range(0, 100)  # Loops van 1 tot 100
output_data = []

# Loop door de verschillende aantallen loops en sla de output op
for loops in loops_range:
    output = run_cpp_program(loops)
    
    # Hier kan je een specifieke waarde uit de uitvoer extraheren
    # Dit is een voorbeeld, je kunt de uitvoer aanpassen afhankelijk van wat je precies nodig hebt
    if "Lengte van new_array:" in output:
        # Bijvoorbeeld: extract het aantal iteraties van de output
        # Aangenomen dat het programma "Aantal loops: X" uitvoert
        start_index = output.find("Lengte van new_array:") + len("Lengte van new_array:")
        end_index = output.find("\n", start_index)
        loops_value = int(output[start_index:end_index].strip())
        output_data.append(loops_value)

# Maak een grafiek van de resultaten
plt.plot(loops_range, output_data, marker='o', linestyle='-', color='b')
plt.title('Resultaten van C++-programma voor verschillende loop aantallen')
plt.xlabel('Aantal Itteraties')
plt.ylabel('Hoeveelheid output')
plt.yscale('log')
plt.grid(True)
plt.savefig("test.png")
