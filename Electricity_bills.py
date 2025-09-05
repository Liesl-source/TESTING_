units=int(input("Please enter the amount of units consumed:"))
if units<50:
    bill=units * 2.60
    Tax= 25
elif units<=100:
    bill=130 + ((units-50)*3.25)
    Tax=35
elif units<=200:
    bill=130+162.50+((units-100)*5.26)
    Tax=45
else:
    bill=130+162.50+526+((units-200)*8.45)
bills=bill+Tax
print (f"Electricity bill:{bills}")