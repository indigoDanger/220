"""
Name: <Indigo Dockery>
<lab5>.py

Problem: <The program uses Python graphics and strings, and displays information about a triangle drawn by the user.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
from math import *


def triangle():
    win = GraphWin("Triangle", 400, 400)
    win.setBackground("white")
    point1 = win.getMouse()
    point2 = win.getMouse()
    point3 = win.getMouse()
    tri = Polygon(point1, point2, point3)
    tri.setFill("red")
    tri.draw(win)
    lenx1 = (point2.getX() - point1.getX())
    lenx2 = (point3.getX() - point2.getX())
    lenx3 = (point1.getX() - point3.getX())
    leny1 = (point2.getY() - point1.getY())
    leny2 = (point3.getY() - point2.getY())
    leny3 = (point1.getY() - point3.getY())
    length1 = sqrt((lenx1 * lenx1) + (leny1 * leny1))
    length2 = sqrt((lenx2 * lenx2) + (leny2 * leny2))
    length3 = sqrt((lenx3 * lenx3) + (leny3 * leny3))
    perim = length1 + length2 + length3
    s = ((length1 + length2 + length3) / 2)
    area = sqrt(s * (s - length1) * (s - length2) * (s - length3))
    texta = Text(Point(300, 250), "Perimeter " + str(perim))
    textb = Text(Point(300, 350), "Area " + str(area))
    texta.draw(win)
    textb.draw(win)
    bye = Text(Point(200, 300), "Click again to close")
    bye.draw(win)
    win.getMouse()
    win.close()


def color_shape():
    # create window
    win_width = 400
    win_height = 400
    win = GraphWin("Color Shape", win_width, win_height)
    win.setBackground("white")

    # create text instructions
    msg = "Enter color values between 0 - 255\nClick window to color shape"
    inst = Text(Point(win_width / 2, win_height - 20), msg)
    inst.draw(win)

    # create circle in window's center
    shape = Circle(Point(win_width / 2, win_height / 2 - 30), 50)
    shape.draw(win)

    # redTexPt is 50 pixels to the left and forty pixels down from center
    red_text_pt = Point(win_width / 2 - 50, win_height / 2 + 40)
    red_text = Text(red_text_pt, "Red: ")
    red_box = Entry(Point(win_width / 2 + 10, win_height / 2 + 40), 5)
    red_text.setTextColor("red")

    # green_text_pt is 30 pixels down from red
    green_text_pt = red_text_pt.clone()
    green_text_pt.move(0, 30)
    green_text = Text(green_text_pt, "Green: ")
    green_box = Entry(Point(win_width / 2 + 10, win_height / 2 + 80), 5)
    green_text.setTextColor("green")

    # blue_text_pt is 60 pixels down from red
    blue_text_pt = red_text_pt.clone()
    blue_text_pt.move(0, 60)
    blue_text = Text(blue_text_pt, "Blue: ")
    blue_box = Entry(Point(win_width / 2 + 10, win_height / 2 + 120), 5)
    blue_text.setTextColor("blue")

    # display rgb text
    red_text.draw(win)
    green_text.draw(win)
    blue_text.draw(win)
    red_box.draw(win)
    green_box.draw(win)
    blue_box.draw(win)

    for i in range(5):
        win.getMouse()
        red_amt = eval(red_box.getText())
        green_amt = eval(green_box.getText())
        blue_amt = eval(blue_box.getText())
        shape.setFill(color_rgb(red_amt, green_amt, blue_amt))

    # Wait for another click to exit
    bye = Text(Point(200, 350), "Click again to close")
    bye.draw(win)
    win.getMouse()
    win.close()


def process_string():
    thing = (input("Enter a string: "))
    first_char = thing[0]
    print("first character:", first_char)
    last_char = thing[-1]
    print("last character:", last_char)
    mid_char = thing[2:5]
    print("Positions 2-5:", mid_char)
    first_last = first_char + last_char
    print("first and last:", first_last)
    first_three = thing[0:3]
    print("first 3, 10 times:", first_three * 10)
    for letter in thing:
        print(letter)
    print("number of characters:", len(thing))


process_string()


def process_list():
    pt = Point(5, 10)
    values = [5, "hi", 2.5, "there", pt, "7.2"]
    x = values
    print(x[1] + x[3])
    print("5 + 2.5 =", x[0] + x[2])
    print(x[1] * 5)
    print(x[2], x[3], x[4])
    print(x[2], x[3], x[0])
    print(x[2], x[0], eval(x[5]))
    print("x =", x[0] + x[2] + eval(x[5]))
    print("number of items in values:", len(values))


process_list()


def another_series():
    terms = eval(input("How many terms? "))
    for i in range(terms):
        pattern = [2, 4, 6, 2, 4, 6]
        start = [0]
        stop = [terms - 1]
        list_terms = pattern[start:stop]
        print("sum =", sum(list_terms))


another_series()


def target():
    win = GraphWin('target', 400, 400)
    win.setBackground('green')
    center = 150
    diameter = 30
    ring1 = Circle(Point(150, 150), center)
    ring1.setFill('white')
    ring1.setOutline('black')
    ring1.draw(win)
    ring2 = Circle(Point(150, 150), center - diameter)
    ring2.setFill('black')
    ring2.setOutline('black')
    ring2.draw(win)
    ring3 = Circle(Point(150, 150), center - 2 * diameter)
    ring3.setFill('blue')
    ring3.setOutline('black')
    ring3.draw(win)
    ring4 = Circle(Point(150, 150), center - 3 * diameter)
    ring4.setFill('red')
    ring4.setOutline('black')
    ring4.draw(win)
    ring5 = Circle(Point(150, 150), center - 4 * diameter)
    ring5.setFill('yellow')
    ring5.setOutline('black')
    ring5.draw(win)
    bye = Text(Point(350, 350), "Click again to close")
    bye.setTextColor("black")
    bye.draw(win)
    win.getMouse()
    win.close()
