# For a string phrase = "AnalyticsData", use slicing to print the first half and second half separately.
# If the string length is odd, make sure the middle character is included in the first half.



# Given string
string = "AnalyticsData"

# Check if the length of the string is even or odd
if len(string) % 2 == 0:
    # If the length is even:
    # Divide the string into two equal parts
    s1 = string[:len(string)//2]   # First half of the string
    s2 = string[len(string)//2:]    # Second half of the string
    
else:
    # If the length is odd:
    # Divide the string into two parts such that the first part has one more character
    s1 = string[0:len(string)//2 + 1]  # First half (with an extra character in the middle)
    s2 = string[len(string)//2:]       # Second half
    
 # Print both parts
print("first half is : ",s1)
print("second half is : ",s2)

