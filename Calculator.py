def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
#Simple calculator
print("Please enter an operation.")
print("a,Addition")
print("b,Subtraction")
print("c,Multiplication")
print("d,Division")
#User input
choice=input("Please enter (a/b/c/d):")
num1=int(input("Please enter the first number:"))
num2=int(input("Please enter the secound number:"))

if choice=='a':
    print(num1,"+",num2,"=",add(num1,num2))
elif choice=='b':
    print(num1,"-",num2,"=",subtract(num1,num2))
elif choice=='c':
    print(num1,"*",num2,"=",multiply(num1,num2))
elif choice=='d':
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("Invalid Input...")