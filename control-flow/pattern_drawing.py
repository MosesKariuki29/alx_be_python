# Ask the user to enter the size of the pattern
size = int(input("Enter the size of the pattern: "))

# Initialize a counter for the while loop
row = 0

# Use a while loop to print each row
while row < size:
    # Use a for loop to print asterisks in one row
    for i in range(size):
        print("*", end="")
    # Move to the next line after finishing a row
    print()
    # Increase the row counter
    row += 1
