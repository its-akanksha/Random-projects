#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
import random
from art12 import logo
print(logo)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 to 100. Can you guess?")

num = random.randint(0,100)

turns = input("Which mode do you wanna play in? Easy or Hard? ").lower()

def compare(x):
    if num>x:
        new_guess = int(input("Too low. Take another guess: "))
        return new_guess
    if num<x:
        new_guess = int(input("Too high. Take another guess: "))
        return new_guess
    if num==x:
        return("Yay! You got the right number. You win!")

def correct_guess(x):
    if num==x:
        print("Yay! You got the right number. You win!")
        return True


guess = int(input("Guess the number: "))


i=0
another_guess=compare(guess)

if turns == 'easy':
    print("You will get 10 guesses to guess the correct number. All the best!")
    while(i<10):
        another_guess = compare(another_guess)
        i=i+1
        if correct_guess(another_guess) is True:
            correct_guess()
    print(f"Sorry, you ran out of turns. The correct number was {num}")

if turns == 'hard':
    print("You will get 5 guesses to guess the correct number. All the best!")

#    if (i<5):
    while(i<=5):
        another_guess = compare(another_guess)
        if correct_guess(another_guess) is True:
            correct_guess()
            break

        elif(i==5):
            print(f"Sorry, you ran out of turns. The correct number was {num}")
            break

        else: i = i + 1

        #    else: print(f"Sorry, you ran out of turns. The correct number was {num}")#
