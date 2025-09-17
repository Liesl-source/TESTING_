low=int(input("Enter the lower range:"))
up=int(input("Enter the upper range:"))
print("Prime numbers between",low,"and",up,"are:")
for i in range(low,up+1):
    if i>1: #(i) will always take the value of the starting range
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)