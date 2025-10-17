# Program to create a list of square values and separate odd and even ones

# Get range from user
start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

# Generate list of squares
squares = [num ** 2 for num in range(start, end + 1)]

# Separate even and odd square values
even_squares = [x for x in squares if x % 2 == 0]
odd_squares = [x for x in squares if x % 2 != 0]

# Display results
print("\nList of square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
