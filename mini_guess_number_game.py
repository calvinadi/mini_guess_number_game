import random
import time

print("welcome to the guessing game,i am going to pick a number between 1 to 100.")

time.sleep(2)
print("picking a number....")
time.sleep(2)

guess_input = int(input("input your guess number: "))

guess_count = 0

correct_number = random.randint(1,100)

while guess_input != correct_number:
  guess_count +=1
  if(guess_input < correct_number):
    print("your guess is too low, try again!")
  else:
    print("your guess is too big, try again!")
  guess_input = int(input("input your guess number: "))


print(f"nice, the correct number is {correct_number}!\nIt took you {guess_count} guesses!")