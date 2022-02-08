"""
Name: <Indigo Dockery>
<lab4>.py

Problem: <This program develops a Python program that uses the author's graphics package.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *


def greeting_card():
    win = GraphWin("Heart", 500, 500)
    win.setBackground("white")

    heart = Polygon(Point(250, 230), Point(200, 210), Point(200, 250), Point(250, 300))
    heart.setFill('red')
    heart.draw(win)

    heart_b = Polygon(Point(250, 230), Point(300, 210), Point(300, 250), Point(250, 300))
    heart_b.setFill('red')
    heart_b.draw(win)

    greeting = Text(Point(250, 350), "Happy Valentine's Day!")
    greeting.setFill('red')
    greeting.setSize(20)
    greeting.draw(win)

    a = Line(Point(120, 350), Point(180, 300))
    a.setOutline("black")
    a.setArrow("last")
    a.draw(win)
    for i in range(1, 20):
        a.move(10, -10)
        time.sleep(0.25)

    win.getMouse()
    win.close()


greeting_card()
