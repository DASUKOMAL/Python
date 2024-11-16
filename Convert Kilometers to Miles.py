# Write a Program to Convert Kilometers to Miles



# Print a message
print("Converting kilometers into miles. \n")

# Prompt the user to enter the number of kilometers and convert the input to a float
k = float(input("Enter number of kilometers: "))

# Define the conversion factor from kilometers to miles
M = 0.621371

# Calculate the equivalent miles by multiplying kilometers by the conversion factor
Miles = k * M

# Print the result in a formatted string
print(f'{k} kilometers is equal to {Miles} miles')

