valid=False
while not valid:
    try:
        n=int(input("Enter a number:"))
        while n%2==0:
            print("BYE")
            break
            
        valid=True
    except ValueError:
        print("Invalid Input. Please enter an integer.")