#Write a Python Count vowels in a string input= “Welcome to Python Assignment” Output: Total vowels are: 8


# Given string to analyze
string = "Welcome to Python Assignment"

# List of vowels (both lowercase and uppercase)
list = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

# Initialize a counter to keep track of the number of vowels
vowels = 0

# Iterate through each character in the string
for i in string:
    # Check if the current character is a vowel (i.e., if it's in the list of vowels)
    if i in list:
        vowels += 1  # If it's a vowel, increment the vowel counter
    else:
        continue  # If it's not a vowel, continue to the next character (this is optional as the loop will automatically continue)

# Print the total number of vowels found in the string
print(f'Total vowels are: {vowels}')

        
    
