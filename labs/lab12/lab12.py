"""
Name: <Indigo Dockery>
<LoopLists>.py

Problem: <This program develops while control structures by using Python's built-in list methods.
It also utilizes python's linear search on data.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
from random import randint


def find_and_remove_first(list, value):
    i = 0
    while i < len(list):
        if list[i] == value:
            list.pop(list[i])
            list[i] = "Indigo Dockery"
        i += 1


def good_input():
    prompt = eval(input("Enter a number in between 1 and 10: "))
    while prompt not in range(1, 11):
        if prompt < 1:
            print("Number is too small, try again:")
        elif prompt > 10:
            print("Number is too big, try again:")
        prompt = eval(input("Enter a number in between 1 and 10: "))
    return prompt


def num_digits():
    playing = True
    while playing:
        prompt = eval(input("Input a positive integer: "))
        num_divisions = 0
        while prompt > 0:
            prompt = prompt // 10
            num_divisions += 1
        print("The number of digits in your number is:", num_divisions)
        if prompt <= 0:
            playing = False


def hi_lo_game():
    secret = randint(1, 100)
    guess = eval(input("Guess the number: "))
    while guess not in range(1, 100):
        tries = 1
        while tries <= 7:
            tries += 1
            if guess > secret:
                print("Too High")
            elif guess < secret:
                print("Too Low")
            guess = eval(input("Guess the number: "))
    print("Correct")
