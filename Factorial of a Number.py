# Write a python program finding the factorial of a given number using a while loop.

#print a message
print(" --- Finding Factorial of a Number --- ")

# Prompt the user to enter a number
num = int(input("Enter a number to find its factorial: "))

# Initialize factorial to 1 (as factorial of 0 is 1)
fact = 1

# Initialize a counter variable to the number
count = num

# Use a while loop to calculate the factorial
while count > 0:
    fact *= count  # Multiply the current factorial by the counter
    count -= 1  # Decrease the counter by 1

# Print the result
print(f'The factorial of {number} is {factorial}')
