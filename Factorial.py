def factorial(x):
    if x ==0 or x==1:
        return 1
    else:
        return x*factorial(x-1)
    #display results
print(factorial.__doc__)
print(f"The factorial of 0 is {factorial(0)}")
print(f"The factorial of 1 is {factorial(1)}")
print(f"The factorial of 2 is {factorial(2)}")
print(f"The factorial of 3 is {factorial(3)}")
print(f"The factorial of 4 is {factorial(4)}")
print(f"The factorial of 5 is {factorial(5)}")
print(f"The factorial of 10 is {factorial(10)}")