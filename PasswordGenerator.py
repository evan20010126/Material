import random

print("How many words of password do you want?")
length = int(input())

lower = "abcdefghijklmnopqrstuvwxyz"
upper = lower.upper()
numbers = "0123456789"
Symbol = "!@#$%^&*()_+[]{}"

all = lower + upper + numbers + Symbol

password = "".join(random.sample(all, length))

print("-----------------------")
print("Password generated: ")
print(password)
