# Convert Roman numerals

numeral_input = input("Enter a Roman numeral: ")
num_input = int(input("Enter an integer: "))

# This program converts Roman numerals to integers and integers to Roman numerals.
def roman_to_int(numeral):
    
    final_answer = 0

    # Check for special cases first (like IV, IX, etc.)
    if "CM" in numeral:
        final_answer += 900
        numeral = numeral.replace("CM", "")
    if "CD" in numeral:
        final_answer += 400
        numeral = numeral.replace("CM", "")
    if "XC" in numeral:
        final_answer += 90
        numeral = numeral.replace("XC", "")
    if "XL" in numeral:
        final_answer += 40
        numeral = numeral.replace("XL", "")
    if "IX" in numeral:
        final_answer += 9
        numeral = numeral.replace("IX", "")
    if "IV" in numeral:
        final_answer += 4
        numeral = numeral.replace("IV", "")

    # Process the remaining characters
    for i in numeral:
        if i == "M":
            final_answer += 1000
        elif i == "D":
            final_answer += 500
        elif i == "C":
            final_answer += 100
        elif i == "L":
            final_answer += 50
        elif i == "X":
            final_answer += 10
        elif i == "V":
            final_answer += 5
        elif i == "I":
            final_answer += 1
        
    print("The Roman numerals you entered translates to: " + str(final_answer) + "!")

# This function converts integers to Roman numerals.
def int_to_roman(num):

    # Check if the number is within the valid range for Roman numerals
    if num < 1 or num > 3999:
        print("Number out of range. Please enter a number between 1 and 3999.")
        return
    
    # Define the values and symbols for Roman numerals
    val = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    syms = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    # Convert the integer to Roman numeral
    result = ""
    for i in range(len(val)):
        count = num // val[i]
        if count > 0:
            result += syms[i] * count
            num -= val[i] * count
    print("The integer you entered translates to: " + result + "!")

roman_to_int(numeral_input)
int_to_roman(num_input)