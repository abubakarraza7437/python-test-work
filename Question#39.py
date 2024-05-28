# Write a program able to play the "Guess the number"game,
# where the number to be guessed is randomly
# chosen between 1 and 20. (Source: http://inventwithpython.com) This is how it should work when run in a
# terminal:
# >>> import guess_number
# Hello! What is your name?
# Torbjörn
# Well, Torbjörn, I am thinking of a number between 1 and 20.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
# Your guess is too low.
# Take a guess.
# 18
# Good job, Torbjörn! You guessed my number in 3 guesses!

from random import randint


def check_answer(guess, number, turn):
    if guess > number:
        print("Your guess is too high. ")
        return turn -1
    elif guess < number:
        print("Your guess is too low. ")
        return turn - 1
    elif guess == number:
        print(f"Good job, {name_of_user}! You guessed my number. ")
        return turn == 0


name_of_user = input("Hello! What is your name? ")
print(f"Well, {name_of_user}, I am thinking of a number between 1 and 20. ")
random_number = randint(1, 21)

life = 5
while life > 0:
    guess_of_user = int(input("Take a guess: "))
    life = check_answer(guess_of_user, random_number, life)
    if life == 0:
        break
    elif life > 0:
        print(f"You have {life}  lives left." )
if life == 0 and guess_of_user != random_number:
    print(f"Sorry, you are out of lives. Correct answer is {random_number}")

