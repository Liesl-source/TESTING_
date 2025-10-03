try:
    number=int(input("Enter a number:"))
    print(f"the number entered is {number}")
except ValueError as ex:
    print("Exception",ex)
