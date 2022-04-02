"""
Name: <Indigo Dockery>
<hangman>.py

Problem: <This program reads files, and utilizes functions, conditional, and decision and repetition structures.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
from random import randint
from graphics import *


def get_words(file_name):
    file = open(file_name, 'r')
    words = file.readlines()
    return words


def get_random_word(words):
    random_word = randint(words[0], words[-1])
    return random_word


def letter_in_secret_word(letter, secret_word):
    for i in secret_word:
        if i == letter:
            return True
    return False


def already_guessed(letter, guesses):
    for i in guesses:
        for j in letter:
            if i == j:
                return True
    return False


def make_hidden_secret(secret_word, guesses):
    obscured = ""
    for i in secret_word:
        is_placed = False
        for j in guesses:
            if i == j:
                is_placed = True
                obscured += j
        if not is_placed:
            obscured += "_"
    return obscured


def won(guessed):
    for i in guessed:
        if i == "_":
            return False
    return True


def play_graphics(secret_word):
    # create the screen
    win = GraphWin("hangman", 400, 400)
    win.setBackground("white")
    # hangman setup
    base = Line(Point(200, 250), Point(325, 250))
    stem = Line(Point(275, 250), Point(275, 50))
    top = Line(Point(275, 50), Point(175, 50))
    hook = Line(Point(175, 50), Point(175, 100))
    # body parts creation
    head = Circle(Point(175, 100), 10)
    body = Line(Point(175, 110), Point(175, 150))
    arm1 = Line(Point(175, 125), Point(168, 115))
    arm2 = Line(Point(175, 125), Point(182, 115))
    leg1 = Line(Point(175, 150), Point(168, 165))
    leg2 = Line(Point(175, 150), Point(182, 165))
    # draw the hangman setup
    base.draw(win)
    stem.draw(win)
    top.draw(win)
    hook.draw(win)
    # set up the word bank
    word_bank = " "
    word_bank2 = " "
    word_bank3 = " "
    word_bank4 = " "
    word_bank5 = " "

    user_entry = Entry(Point(50, 300), 2)
    user_entry.draw(win)

    guessed_letters = []
    num_guesses_left = 6
    word = Text(Point(50, 200), "")
    word.draw(win)
    letter1 = "a"
    letter2 = "b"
    letter3 = "c"
    letter4 = "d"
    letter5 = "e"
    letter6 = "f"
    letter7 = "g"
    letter8 = "h"
    letter9 = "i"
    letter10 = "j"
    letter11 = "k"
    letter12 = "l"
    letter13 = "m"
    letter14 = "n"
    letter15 = "o"
    letter16 = "p"
    letter17 = "q"
    letter18 = "r"
    letter19 = "s"
    letter20 = "t"
    letter21 = "u"
    letter22 = "v"
    letter23 = "w"
    letter24 = "x"
    letter25 = "y"
    letter26 = "z"
    word_bank += str(letter1) + str(letter2) + str(letter3) + str(letter4) + str(letter5) + str(letter6) + str(letter7)
    word_bank2 += str(letter8) + str(letter9) + str(letter10) + str(letter11) + str(letter12) + str(letter13)
    word_bank3 += str(letter14) + str(letter15) + str(letter16) + str(letter17) + str(letter18) + str(letter19)
    word_bank4 += str(letter20) + str(letter21) + str(letter22) + str(letter23) + str(letter24) + str(letter25)
    word_bank5 += str(letter26)
    bank1 = Text(Point(20, 10), word_bank)
    bank1.draw(win)
    bank2 = Text(Point(20, 20), word_bank2)
    bank2.draw(win)
    bank3 = Text(Point(20, 30), word_bank3)
    bank3.draw(win)
    bank4 = Text(Point(20, 40), word_bank4)
    bank4.draw(win)
    bank5 = Text(Point(20, 50), word_bank5)
    bank5.draw(win)
    statement1 = Text(Point(150, 300), " ")
    statement2 = Text(Point(150, 350), " ")
    statement1.draw(win)
    statement2.draw(win)
    while num_guesses_left > 0 and not won(make_hidden_secret(secret_word, guessed_letters)):
        word.setText(make_hidden_secret(secret_word, guessed_letters))
        win.getMouse()
        guess = user_entry.getText()
        statement3 = Text(Point(150, 325), " ")
        statement3.setText(str(make_hidden_secret(secret_word, guessed_letters)))
        statement3.draw(win)
        if not already_guessed(guess, guessed_letters):
            guessed_letters.append(guess)
            if not letter_in_secret_word(guess, secret_word):
                num_guesses_left = num_guesses_left - 1
                statement1.setText("already guessed:" + str(guessed_letters))
                statement2.setText("guesses left:" + str(num_guesses_left))
                if num_guesses_left == 5:
                    head.draw(win)
                elif num_guesses_left == 4:
                    body.draw(win)
                elif num_guesses_left == 3:
                    arm1.draw(win)
                elif num_guesses_left == 2:
                    arm2.draw(win)
                elif num_guesses_left == 1:
                    leg1.draw(win)
                elif num_guesses_left == 0:
                    leg2.draw(win)
                if guess in word_bank:
                    bank1.setTextColor("red")
                elif guess in word_bank2:
                    bank2.setTextColor("red")
                elif guess in word_bank3:
                    bank3.setTextColor("red")
                elif guess in word_bank4:
                    bank4.setTextColor("red")
                elif guess in word_bank5:
                    bank5.setTextColor("red")
    if won(make_hidden_secret(secret_word, guessed_letters)):
        winner = Text(Point(300, 300), "winner!")
        secret = Text(Point(300, 325), secret_word)
        winner.draw(win)
        secret.draw(win)
        win.getMouse()
        win.close()
    else:
        loser = Text(Point(300, 300), "sorry, you lost :(")
        secret = Text(Point(300, 325), secret_word)
        loser.draw(win)
        secret.draw(win)
        win.getMouse()
        win.close()


def play_command_line(secret_word):
    guessed_letters = []
    num_guesses_left = 6
    while num_guesses_left > 0 and not won(make_hidden_secret(secret_word, guessed_letters)):
        print("already guessed:", guessed_letters)
        print("guesses remaining:", num_guesses_left)
        print(make_hidden_secret(secret_word, guessed_letters))
        guess = input("guess a letter: ")
        if not already_guessed(guess, guessed_letters):
            guessed_letters.append(guess)
            if not letter_in_secret_word(guess, secret_word):
                num_guesses_left = num_guesses_left - 1
    if won(make_hidden_secret(secret_word, guessed_letters)):
        print("winner!")
        print(secret_word)
    else:
        print("sorry, you lost :(")
        print(secret_word)


if __name__ == '__main__':
    pass
