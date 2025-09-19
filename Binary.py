number=int(input("Please enter a decimal mumber:"))
while number != 0:
    remainder = number % 2  # gives the exact remainder
    number = number // 2
    result= str(remainder)+result
print("The binary representation is", result)