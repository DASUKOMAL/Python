''' A transport company charges the fare according to following table: 

Distance                    Charges 

1-50                           8 Rs./Km 
51-100                       10 Rs./Km 
> 100                          12 Rs/Km

'''

# Display a message
print(" ---- Transporting charges for a Customer  ---- \n")

# Prompt the user to enter the number of kilometers for the drop-off and convert it to a float
km = float(input("Enter how many Kilometers to Drop : "))

# Initialize the price variable to store the fare
price = 0

# Determine the price based on the number of kilometers
if km >= 1 and km <= 50:
    price = km * 8  # Calculate fare for 1 to 50 kilometers at 8 per kilometer
    print(f'Total fare for {km} Kilometers is {price}')  # Display the total fare
elif km >= 51 and km <= 100:
    price = km * 10  # Calculate fare for 51 to 100 kilometers at 10 per kilometer
    print(f'Total fare for {km} Kilometers is {price}')  # Display the total fare
else:
    price = km * 12  # Calculate fare for more than 100 kilometers at 12 per kilometer
    print(f'Total fare for {km} Kilometers is {price}')  # Display the total fare

    
