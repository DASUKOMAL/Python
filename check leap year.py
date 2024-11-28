# Python program to check leap year



# Print a message 
print("Checking for leap year. \n")

# Prompt the user to enter a year and convert the input to an integer
year = int(input("Enter a year: "))

# Check if the year is a leap year based on the rules
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
