import random


def get_answer():
    value = random.randint(1, 100)
    return value


answer = get_answer()
guess = -1

while guess != answer:
    guess = input("guess a number between 1 and 100: ")
    guess = int(guess)
    if guess > answer:
        print("Too high")
    elif guess < answer:
        print("Too low")
    else:
        print("Your answer",guess,"is correct!")
