X=5
if (type(X)is int):
    print("True")
else:
    print("False")

Y=5.0
if(type(Y)is not float):
    print("True")
else:
    print("False")

x=20
y=20
if (x is y):
    print("X and y is same identity")
y=30
if (x is not y):
    print("X and y is not the same identity")