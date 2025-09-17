n=int(input("Please enter the amount of rows you want to print:"))
for i in range (n):
    for j in range(i+1):
        print("*",end="")
    print()
