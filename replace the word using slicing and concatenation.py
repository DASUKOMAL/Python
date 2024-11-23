# Given a string msg = "Hello Python World", replace the word "Python" with "Data" by using slicing and concatenation.


# Given strings
string = "Hello Python World"  # Original string
string2 = "Data"               # String to replace "Python" with

# Create a new string by concatenating three parts:
# 1. The part of 'string' before the word "Python"
# 2. The new word "Data"
# 3. The part of 'string' after the word "Python"
s = string[0:6] + string2 + string[12:len(string)]

# Print the modified string
print("After replacing word with 'Python' the new world is : ",s)

