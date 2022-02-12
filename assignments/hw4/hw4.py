"""
Name: <Indigo Dockery>
<hw4>.py

Problem: <This program uses Python graphics and the author-supplied graphics package to practice accumulating sequences.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke at CSS>
"""

from graphics import *
from math import *
import math

def squares():
    # Creates a graphical window
    width = 400
    height = 400
    win = GraphWin("Clicks", width, height)

    # number of times user can move square
    num_clicks = 5

    # create a space to instruct user
    inst_pt = Point(width / 2, height - 10)
    instructions = Text(inst_pt, "Click to move square")
    instructions.draw(win)

    # builds a square
    shape = Rectangle(Point(50, 50), Point(100, 100))
    shape.setOutline("red")
    shape.setFill("red")
    shape.draw(win)

    # allows the user to click multiple times to move the square
    for i in range(num_clicks + 1):
        click = win.getMouse()


        # move amount is distance from center of square to the
        # point where the user clicked
        change_x = click.getX()
        change_y = click.getY()
        rect = Rectangle(Point(change_x - 25, change_y - 25), Point(change_x + 25, change_y + 25))
        rect.setFill("red")
        rect.draw(win)
    bye = Text(Point(200, 450),("Click again to close"))
    bye.draw(win)
    win.getMouse()
    win.close()


def rectangle():
    win = GraphWin("Rectangle", 500, 500)
    point1 = win.getMouse()
    point2 = win.getMouse()
    rect = Rectangle(point1, point2)
    rect.setFill("red")
    rect.draw(win)
    len = abs(point1.getX() - point2.getX())
    wid = abs(point1.getY() - point2.getY())
    perim = (2 * len) + (2 * wid)
    area = len * wid
    texta = Text(Point(300, 250),"Perimeter " + str(perim))
    textb = Text(Point(300, 350),"Area " + str(area))
    texta.draw(win)
    textb.draw(win)
    bye = Text(Point(200, 450),("Click again to close"))
    bye.draw(win)
    win.getMouse()
    win.close()


def circle():
    win = GraphWin("Circle", 500, 500)
    center = win.getMouse()
    circum = win.getMouse()
    r = sqrt((circum.getX() - center.getX())**2 + (circum.getY() - center.getY())**2)
    circle = Circle(center, r)
    circle.setFill("red")
    circle.draw(win)
    textr = Text(Point(400, 250), "Radius:" + str(r))
    textr.draw(win)
    bye = Text(Point(200, 450),("Click again to close"))
    bye.draw(win)
    win.getMouse()
    win.close()

def pi2():
    total = 0
    n = eval(input("enter the number of terms to sum: "))
    num_add = int(n/2) + (n%2)
    num_sub = int(n/2)
    for i in range(num_add):
        denom = (4 * i) + 1
        frac = 4 / denom
        total = total + frac
    for i in range(num_sub):
        denom = (4 * i) + 3
        frac = 4 / denom
        total = total - frac
    print("pi approximation: ", total)
    approx = abs(math.pi - total)
    print("accuracy: ", approx)

if __name__ == '__main__':
    pass
