#Write a python program to check whether a number is palindrome or not?




# Prompt the user to enter a number
print("Enter a number") 
num = int(input())  # Read the input and convert it to an integer

rev = 0  # Initialize a variable to hold the reversed number
temp = num  # Store the original number for later comparison

# Loop to reverse the number
while num > 0:
    rem = num % 10  # Get the last digit of the number
    rev = (rev * 10) + rem  # Append the last digit to the reversed number
    num = num // 10  # Remove the last digit from the original number

# Print the reversed number
print(f'The reverse of {temp} is {rev}')

# Check if the original number is equal to the reversed number
if temp == rev:
    print(f'{temp} is a palindrome')  # Print if the number is a palindrome
else:
    print(f'{temp} is not a palindrome')  # Print if the number is not a palindrome

