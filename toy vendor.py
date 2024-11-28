''' A toy vendor supplies three types of toys: Battery Based Toys, Key-based Toys, and Electrical
Charging Based Toys. The vendor gives a discount of 10% on orders for battery-based toys if the
order is for more than Rs. 1000. On orders of more than Rs. 100 for key-based toys, a discount of 5% is given,
and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500. Assume
that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based
toys respectively. Write a program that reads the productcode and the order amount and prints out the net amount
that the customer is required to pay after the discount.'''

import sys  # Import the sys module for system-specific parameters and functions

# Welcome message
print("\n --- Welcome to Toys store --- \n")
print(" 1.Battery Based Toys \n 2.Key-based Toys \n 3.Electrical Charging Based Toys \n 4.Exit \n")
print("Select any Item from the list")

# User input for selection
s = int(input())

# Process selection for Battery Based Toys
if s == 1:
    print("You have selected Battery Based Toys")
    item = input("Enter name of the Item : ")  # Get item name
    amount = int(input("Enter ordered Amount : "))  # Get ordered amount
    discount = 0  # Initialize discount

    # Check if amount is eligible for discount
    if amount > 1000:
        discount = 0.10 * amount  # Calculate 10% discount
        amount = amount - discount  # Apply discount
        print(f'Your Amount After discount is {amount}')  # Show final amount after discount
        print(" ---- THANK YOU ---- ")
        
    else:
        print(f'No discount available')  # Notify if no discount
        print(f'your Amount is {amount}')  # Show amount without discount
        print(" ---- THANK YOU ---- ")

# Process selection for Key-based Toys
elif s == 2:
    print("You have selected Key-based Toys")
    item = input("Enter name of the Item : ")
    amount = int(input("Enter ordered Amount : "))
    discount = 0

    # Check if amount is eligible for discount
    if amount > 100:
        discount = 0.05 * amount  # Calculate 5% discount
        amount = amount - discount  # Apply discount
        print(f'Your Amount After discount is {amount}')
        print(" ---- THANK YOU ---- ")
        
    else:
        print(f'No discount available')
        print(f'your Amount is {amount}')
        print(" ---- THANK YOU ---- ")

# Process selection for Electrical Charging Based Toys
elif s == 3:
    print("You have selected Electrical Charging Based Toys")
    item = input("Enter name of the Item : ")
    amount = int(input("Enter ordered Amount : "))
    discount = 0

    # Check if amount is eligible for discount
    if amount > 500:
        discount = 0.10 * amount  # Calculate 10% discount
        amount = amount - discount  # Apply discount
        print(f'Your Amount After discount is {amount}')
        print(" ---- THANK YOU ---- ")
        
    else:
        print(f'No discount available')
        print(f'your Amount is {amount}')
        print(" ---- THANK YOU ---- ")

# Exit option
elif s == 4:
    sys.exit(0)  # Exit the program
    print(" ---- THANK YOU ---- ")

# Handle invalid selection
else:
    print("Invalid choice!!!!")  # Notify user of invalid input

