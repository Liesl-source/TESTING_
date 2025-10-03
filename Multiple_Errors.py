try:
    num1, num2= eval(input("Enter two numbers, separated by a comma: "))
    result=num1 / num2
    print(f"The result is {result}")

except ZeroDivisionError:
    print("Division by zero is an ERROR!!!")
except SyntaxError:
    print("Comma is missing. Enter numbers separated by a comma like this 1, 2")
except:
    print("Wrong input...")
else:
    print("No exceptions")
finally:
    print("Execution completed")
