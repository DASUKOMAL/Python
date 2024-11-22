'''Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string
Input = “Hell0 W0rld ! 123 * # welcome to pYtHoN” Output: UpperCase : 5 LowerCase : 18 NumberCase : 5 SpecialCase : 11
'''
# Given string to analyze
string = "Hell0 W0rld ! 123 * # welcome to pYtHoN"

# Initialize counters for each category
UpperCase = 0   # Counter for uppercase letters
LowerCase = 0   # Counter for lowercase letters
NumberCase = 0  # Counter for digits (numbers)
SpecialCase = 0 # Counter for special characters (non-alphabetic and non-digit)

# Iterate through each character in the string
for i in string:
    # Check if the character is an uppercase letter (A-Z)
    if i.isupper():
        UpperCase += 1  # Increment the uppercase counter
    # Check if the character is a lowercase letter (a-z)
    elif i.islower():
        LowerCase += 1  # Increment the lowercase counter
    # Check if the character is a digit (0-9)
    elif i.isdigit():
        NumberCase += 1  # Increment the digit counter
    else:  # If the character is neither a letter nor a digit, it's treated as a special character
        SpecialCase += 1  # Increment the special character counter

# Print the results
print(f'UpperCase : {UpperCase}')   # Print the count of uppercase letters
print(f'LowerCase : {LowerCase}')   # Print the count of lowercase letters
print(f'NumberCase : {NumberCase}') # Print the count of digits
print(f'SpecialCase : {SpecialCase}') # Print the count of special characters

