#program to find check whether the user is eligible to vote.

# telling for user to enter their name
print("Enter your Name")
# Store user's input in the 'name' variable
name = input()

# telling for user to enter their age
print("Enter age")
# Store user's input as an integer in the 'age' variable
age = int(input())

# Check eligibility to vote based on age
if age < 18: 
    # Print message if user is underage
    print("You are NOT eligible to vote.")
else: 
    # Print message if user is eligible
    print("You are eligible to vote.")

