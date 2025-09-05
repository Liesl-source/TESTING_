Medical_issues=(input("Do you have any medical issues? Y/n:"))
Atten=int(input("Please enter your attendance percentage:"))
if Medical_issues=="Y":
    print("You are eligible for the exam.")
else:
    if Atten>=75:
        print("You are eligible for the exam.")
    else:
        print("You are not eligible for the exam.")