# Given a string text = "Data Analytics in Python", extract the substring "Analytics" using slicing.
#Extract the word "Python" from text using a negative index in slicing.


# Given string
string = "Data Analytics in Python"

# Extract a substring using slicing (positive indices)
s = string[4:14]  # Extracts from index 4 to index 13 (not inclusive of index 14)
# This gives the substring "Analytics "

# Extract a substring using negative indexing
s1 = string[-6:]  # Extracts the last 6 characters of the string (negative indexing)
# This gives the substring "Python"

# Print the results
print("The extracted substring using slicing is:", s)  # Output the substring from indices 4 to 14
print("The extracted substring using negative slicing is:", s1)  # Output the last 6 characters

