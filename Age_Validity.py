def check_age():
    try:#  Take input from user
        age = int(input("Enter your age: "))
        #  Validate age
        if age < 0 or age > 120:
            print("Error: Age entered is not realistic.")
        else:
            # Check if even or odd
            if age % 2 == 0:
                print(f"Your age ({age}) is even.")
            else:
                print(f"Your age ({age}) is odd.")

    except ValueError:
        print("Error: Please enter a valid number for age.")