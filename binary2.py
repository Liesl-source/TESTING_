n = int(input("Please enter a decimal number:"))  # decimal number
res = ''  # binary result

while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)
