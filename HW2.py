#Create a list of squares of numbers from 1 to 10
squares = [x**2 for x in range(1, 11)]
print("Squares from 1 to 10:", squares)

#Create a list of even numbers from 1 to 20
evens = [x for x in range(1, 21) if x % 2 == 0]
print("Even numbers from 1 to 20:", evens)
# Create a list of odd numbers from 1 to 20
odds = [x for x in range(1, 21) if x % 2 != 0]
print("Odd numbers from 1 to 20:", odds)
#Convert a list of temperatures from Celsius to Fahrenheit

celsius = [0, 10, 20, 30, 40]

fahrenheit = [(temp * 9/5) + 32 for temp in celsius]
print("Fahrenheit temperatures:", fahrenheit)
#Create a list of numbers greater than 10 from a given list

numbers = [5, 12, 7, 18, 3, 25]

greater_than_10 = [x for x in numbers if x > 10]
print("Numbers greater than 10:", greater_than_10)
#Convert all strings in a list to uppercase

names = ["tesy", "john", "liesl"]

uppercase_names = [name.upper() for name in names]
print("Uppercase names:", uppercase_names)
#Create a list of lengths of each word in a list

words = ["python", "list", "comprehension"]

lengths = [len(word) for word in words]
print("Lengths of words:", lengths)