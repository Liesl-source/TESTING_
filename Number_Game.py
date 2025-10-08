import random
playing=True
number=str(random.randint(10,20))

print("Welcome to the number guessing game!")
print("I'm going to generate a number between 10 and 20... And you have to guess it one digit at a time!")
print("The game ends when you guess atleast one digit correctly!")
while playing:
    guess=input("Give me your best guess! \n")
    if number==guess:
        print(f"You guessed it! The number was {number}!!!")
        print("Great job! (˶ˆᗜˆ˵)")
        break
    else:
        print("You got it wrong...(╥﹏╥) Try again! \n")

