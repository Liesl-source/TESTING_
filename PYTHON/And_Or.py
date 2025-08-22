#AND_logical_operator
a=10
b=12
c=2
if a and b and c:
    print("All the variables have the boolean value True.")
elif b and c:
    print("Only b has the boolean value of True but c is False")
else:
    print("Atleast one of the variables have the boolean value False.")
#OR_logical_operator
a=10
b=0
c=-5
if a> 0 or b> 0:
    print("Atleast one of the variables is greater than 0.")
else:
    print("None of the variables is greater than 0.")
if b>0 or c>0:
    print("Atleast one of the values are greater than 0.")
else:
    print("None of the values is greater than 0.")
