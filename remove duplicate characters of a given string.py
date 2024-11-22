# Write a Python program to remove duplicate characters of a given string. Input = “String and String Function” Output: String and Function


# Given string with repeated words
string = "String and String Function"

# Split the string into a list of words using the space character as a delimiter
s = string.split(" ")

# Initialize an empty list to store unique words
list = []

# Loop through each word in the split string list
for i in s:
    # Check if the word already exists in the list (i.e., it has already been added)
    if i in list:
        continue  # If the word is already in the list, skip adding it again
    else:
        # If the word is not in the list, append it to the list
        list.append(i)

# Join the unique words back together into a single string, separating them by spaces
res = ' '.join(list)

# Print the resulting string of unique words
print(res)

    
