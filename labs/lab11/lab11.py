"""
Name: <Indigo Dockery>
<lab10>.py

Problem: <This program creates a user-defined class and utilizes a list of objects.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""

from graphics import*
from button import Button
from door import Door
from random import randint


def three_door_game():
    win = GraphWin("Three Door Game", 500, 600)
    win.setBackground("lightblue")

    button = Button(Rectangle(Point(300, 50), Point(400, 100)), "Quit Game")
    button.draw(win)

    scoreboard = Rectangle(Point(20, 20), Point(125, 50))
    winner_text = Text(Point(45, 10), "wins")
    chart_line = Line(Point(75, 10), Point(75, 50))
    loser_text = Text(Point(105, 10), "losses")
    chart_line.draw(win)
    scoreboard.draw(win)
    winner_text.draw(win)
    loser_text.draw(win)
    wins = 0
    losses = 0

    door_shape = Rectangle(Point(20, 250), Point(80, 500))
    door_shape2 = Rectangle(Point(100, 250), Point(160, 500))
    door_shape3 = Rectangle(Point(180, 250), Point(240, 500))

    door1 = Door(door_shape, "Door 1")
    door1.draw(win)
    door1.color_door("brown")
    door2 = Door(door_shape2, "Door 2")
    door2.draw(win)
    door2.color_door("brown")
    door3 = Door(door_shape3, "Door 3")
    door3.draw(win)
    door3.color_door("brown")

    winner = Text(Point(50, 30), wins)
    winner.draw(win)

    loser = Text(Point(80, 30), losses)
    loser.draw(win)

    closet = [door1, door2, door3]
    click = win.getMouse()
    while not button.is_clicked(click):

        secret = randint(0, 2)
        secret_door = closet[secret]
        message = Text(Point(250, 125), "I have a secret door")
        message.draw(win)
        if secret_door.is_clicked(click):
            color = "green"
            secret_door.color_door(color)
            message.setText("you win!")
            wins = wins + 1
            winner.setText(wins)
        elif not secret_door.is_clicked(click):
            losses = losses + 1
            loser.setText(losses)

            wrong_color = "pink"
            color = "green"

            if door1.is_clicked(click):
                door1.color_door(wrong_color)
            elif door2.is_clicked(click):
                door2.color_door(wrong_color)
            else:
                door3.color_door(wrong_color)

            secret_door.color_door(color)
            message.setText("sorry, incorrect!")

        repeat_display = Text(Point(350, 550), "click anywhere to play again")
        repeat_display.draw(win)
        click = win.getMouse()
        if button.is_clicked(click):
            win.close()
        else:
            door1.color_door("brown")
            door2.color_door("brown")
            door3.color_door("brown")
            secret_door.set_secret(False)
            message.undraw()
            click = win.getMouse()

    win.close()
