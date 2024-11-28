# Python Program to Check if a Number is Positive, Negative or 0



# Print a message 
print("Checking if the number is Positive, Negative, or 0. \n")

# Prompt the user to enter a number and convert the input to an integer
num = int(input("Enter a number: "))

# Check if the number is greater than zero
if num > 0:
    print('The number is Positive')
# Check if the number is less than zero
elif num < 0:
    print('The number is Negative')
# If the number is neither, it must be zero
else:
    print('The number is Zero (0)')

