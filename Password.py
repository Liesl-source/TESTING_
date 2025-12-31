import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"

# Set password length lol
length = 8

password = ""

# generate dat stuuupid password >:)
for i in range(length):
    password = password + random.choice(lower + upper + numbers)

# Shuffle dat thang
random.shuffle(list(password))

print("Your password is:", password)