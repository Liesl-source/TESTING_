print("Write in your grades to know your performance!")
m1=int(input("Enter the marks of Math:"))
m2=int(input("Enter the marks of Science:"))
m3=int(input("Enter the marks of English:"))
mk4=int(input("Enter the marks of History:"))
m5=int(input("Enter the marks of Geography:"))
total= m1+m2+m3+mk4+m5
avg= total/5
if avg>=90 and avg<=100:
    print(f"Your average is {avg} and your grade is A+")
elif avg>=81 and avg<=91:
    print(f"Your average is {avg} and your grade is A")
elif avg>=71 and avg<=81:
    print(f"Your average is {avg} and your grade is B+")
elif avg>=61 and avg<=71:
    print(f"Your average is {avg} and your grade is B")
elif avg>=51 and avg<=61:
    print(f"Your average is {avg} and your grade is C+")
elif avg>=41 and avg<=51:
    print(f"Your average is {avg} and your grade is C")
elif avg>=31 and avg<=41:
    print(f"Your average is {avg} and your grade is D+")
elif avg>=21 and avg<=31:
    print(f"Your average is {avg} and your grade is D")
elif avg>=0 and avg<=21:
    print(f"Your average is {avg} and your grade is F meaning...YOU FAILED!!!!!")
else:
    print("Invalid Input...")