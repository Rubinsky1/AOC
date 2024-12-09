import itertools

# Functie om een reeks van getallen en operatoren te evalueren
def evaluate_expression(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '|':
            result = str(result) + str(numbers[i+1]) 
            result = int(result)
    return result


def calibrations(lines, choice):
    total_calibration = 0

    # Verwerk elke regel
    for line in lines:
        line = line.strip()
        key, values = line.split(":")
        test_value = int(key.strip())
        numbers = list(map(int, values.split()))

        # Genereer alle mogelijke combinaties van operatoren
        if choice == 0:
            operators_combinations = list(itertools.product(['+', '*'], repeat=len(numbers) - 1))
        if choice == 1:
            operators_combinations = list(itertools.product(['+', '*', '|'], repeat=len(numbers) - 1))
        # Controleer of een van de operator combinaties de testwaarde oplevert
        for operators in operators_combinations:
            if evaluate_expression(numbers, operators) == test_value:
                total_calibration += test_value
                break

    return(total_calibration)