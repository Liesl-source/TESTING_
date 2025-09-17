rows=int(input("Enter the number of rows:"))
#Top half
for i in range(1,rows+1,2):
    print(" "*((rows-i)//2),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()
#Bottom half
for i in range(rows-2, 0,-2):
    print(" "*((rows-i)//2),end=" ")
    for j in range(1,i+1):
        print(j,end="")
    print()