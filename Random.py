x = 100
y = 50
print(x and y)

rows = 5  # Define the number of rows
I = rows
while I > 0:
    j = I
    while j > 0:
        print("*", end=" ")
        j -= 1  # Decrement j to avoid infinite loop
    print()  # Move to the next line after each row
    I -= 1  # Decrement I to avoid infinite loop
a=0
for c in range(10):
    for d in range(-1,-10,-1):
        a+=1
    print(a)


