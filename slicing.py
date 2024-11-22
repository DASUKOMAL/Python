'''Given a string word = "DataScience", extract every second character from the string using slicing.
Try to extract every third character from word, starting from the second character.1 '''


# Given word
word = "DataScience"

# Extract every second character from the string starting from index 1
s = word[1:len(word):2]  # Starts at index 1 and selects every second character (i.e., step size = 2)

# Extract every third character starting from index 2
s1 = word[2:len(word):3]  # Starts at index 2 and selects every third character (step size = 3)

# Print the results
print("Extracting every second character from the string is:", s)  # Output the characters selected by step 2
print("Extracting every third character from the second character of the string is:", s1)  # Output the characters selected by step 3




