def demo_break():
    for i in range(1, 11):  # Loop from 1 to 10
        if i == 6:
            print("Breaking the loop at i =", i)
            break  # Exit the loop when i is 6
        print("Current value of i:", i)
    print("Loop has ended.")

# Call the function
demo_break()