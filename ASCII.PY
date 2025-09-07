Char=input("Please enter a character:")
if len(Char)==1: # Now learned the "Length" function
    ASCII_value=ord(Char) # ord() function gives the ASCII value of a character
    print("The ASCII value of", Char, "is:", ASCII_value)
else:
    print("Please enter a single character only.") #You can only find the Ascii value of a single character
