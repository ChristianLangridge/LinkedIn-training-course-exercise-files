hexNumbers = {
    '0': 0, "1": 1, "2": 2, "3": 3, "4": 4,
    "5": 5, "6": 6, "7": 7,
    "8": 8, "9": 9, "A": 10,
    "B": 11, "C": 12, "D": 13,
    "E": 14, "F": 15
}

# Converts a string hexadecimal number into an integer decimal 
# If hexNum is not a valid hexadecimal number, returns None

def hexToDec(hexNum):

    total = 0 

    for char in hexNum:
        if char not in hexNumbers:
            return None
    
    for i in range(len(hexNum)):
        exponent = len(hexNum) - 1 - i
        digit_value = hexNumbers[hexNum[i]]
        total += digit_value * (16 ** exponent)
    return total 


        

hexToDec('ABC')