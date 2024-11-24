# Write a Python program to Count all letters, digits, and special symbols from the given string
#Input = “P@#yn26at^&i5ve” Output: Chars = 8 Digits = 2 Symbol = 3


# Given string to analyze
string = "P@#yn26at^&i5ve"

# Initialize counters for characters (letters), digits, and symbols
Chars = 0  # To count alphabetic characters (letters)
Digits = 0  # To count numeric digits
Symbols = 0  # To count special symbols (non-alphabetic and non-numeric characters)

# Iterate through each character in the string
for i in string:
    # Check if the character is an alphabetic letter (a-z or A-Z)
    if i.isalpha():
        Chars += 1  # Increment the character count if it's a letter
    # Check if the character is a digit (0-9)
    elif i.isdigit():
        Digits += 1  # Increment the digit count if it's a number
    # If it's neither a letter nor a digit, it's considered a symbol
    else:
        Symbols += 1  # Increment the symbol count for special characters like @, #, ^, & etc.

# Print the results after the loop completes
print(f'The number of Characters in the string is: {Chars}')  # Print the total number of letters
print(f'The number of Digits in the string is: {Digits}')  # Print the total number of digits
print(f'The number of Symbols in the string is: {Symbols}')  # Print the total number of symbols

