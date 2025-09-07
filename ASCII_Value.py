
print("Welcome to the Manual ASCII Finder!")

ascii_table = {
'A': 65,
'B': 66,
'C': 67,
'D': 68,
'E': 69,
'F': 70,
'a': 97,
'b': 98,
'c': 99,
'd': 100,
'e': 101,
'f': 102,
'0': 48, 
'1': 49,
'2': 50,
'!': 33,
'@': 64,
'#': 35,
' ': 32  #Space
}

char = input("Please enter a character: ")

if char in ascii_table:
    print("The ASCII value of", char, "is", ascii_table)
else:
    print("Sorry, I don't know the ASCII value of that character.")