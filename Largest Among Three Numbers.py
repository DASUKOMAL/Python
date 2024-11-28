#Python Program to Find the Largest Among Three Numbers

# Display a message
print("Checking for Largest Number \n")

# Prompt the user to enter the first number and convert it to an integer
num1 = int(input("Enter first number "))
# Prompt the user to enter the second number and convert it to an integer
num2 = int(input("Enter second number "))
# Prompt the user to enter the third number and convert it to an integer
num3 = int(input("Enter third number "))

# Check if num1 is greater than both num2 and num3
if (num1 > num2 and num1 > num3):
    print(f'{num1} is the largest Number')  # Print num1 if it is the largest
# Check if num2 is greater than both num1 and num3
elif (num2 > num1 and num2 > num3):
    print(f'{num2} is the largest Number')  # Print num2 if it is the largest
# Check if num3 is greater than both num1 and num2
elif (num3 > num1 and num3 > num2):
    print(f'{num3} is the largest Number')  # Print num3 if it is the largest
# If none of the above conditions are true, it means all numbers are equal
else:
    print("All numbers are equal")  # Print message if all numbers are equal

