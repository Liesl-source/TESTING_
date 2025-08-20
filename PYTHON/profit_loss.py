actual_profit= float(input("Please enter the actual amount..."))
sale_price= float(input("Please enter you sale amount..."))
if actual_profit<sale_price:
    Amount= sale_price-actual_profit
    print(f"The total profit gained is {Amount}")
else:
    print("No profit!! You're broke...")