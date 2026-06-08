# Morse Code Translator

# Morse code dictionary mapping letters and numbers to their Morse code representations
morse_code_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.',
                   'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.',
                   'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.', 'S':'...', 'T':'-', 'U':'..-',
                   'V':'..-', 'W':'.--', 'X':'-..-', 'Y':'-.--', 'Z':'--..',
                   
                   '1':'.----', '2':'..---', '3':'...--', '4':'....-', '5':'.....', '6':'-....',
                   '7':'--...', '8':'---..', '9':'----.', '0':'----',}

# Function to translate text to Morse code
def text_to_morse(text):
    result = ""
    for char in text:
        if char in morse_code_dict:
            result += morse_code_dict[char] + " "
        elif char == " ":
            result += "/ "
    print(result)

# Main function to get user input and call the translation function
def main():
    user = input("Enter text to translate to Morse code: ").upper()
    text_to_morse(user)

main()