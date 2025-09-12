string=input("Enter your word:")
i=0
char=input("Enter the character you want to count:")
count=0
while i<len(string):
    if string[i]==char:
        count+=1
    i+=1
print(f"The Character {char} appears {count} times in {string}.")