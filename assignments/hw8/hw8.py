"""
Name: <Indigo Dockery>
<hw7>.py

Problem: <This program writes functions, and is capable of reading and writing text files.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
from graphics import *
import math


def add_ten(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] + 10


def square_each(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2


def sum_list(nums):
    sum_1 = 0
    for i in range(len(nums)):
        sum_1 = sum_1 + nums[i]
    return sum_1


def to_numbers(nums):
    for i in range(len(nums)):
        nums[i] = float(nums[i])


def sum_of_squares(nums):
    list_a = []
    for i in range(len(nums)):
        line_split = nums[i].split(', ')
        to_numbers(line_split)
        square_each(line_split)
        value = sum_list(line_split)
        list_a.append(value)
    return list_a


def starter(weight, wins):
    if((weight >= 150) and (weight < 168)) and (wins >= 5):
        return True
    if (weight > 199) or (wins > 20):
        return True
    return False


def leap_year(year):
    if (year % 4 == 0) and (year % 100 != 0):
        return True
    elif(year % 400 == 0) and (year % 100 == 0):
        return True
    return False


def circle_overlap():
    width_px = 700
    height_px = 700
    win = GraphWin("Circle", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    center = win.getMouse()
    circumference_pt = win.getMouse()
    radius = math.sqrt(
        (center.getX() - circumference_pt.getX()) ** 2 + (center.getY() - circumference_pt.getY()) ** 2)

    circle_one = Circle(center, radius)
    circle_one.setFill("light blue")
    circle_one.draw(win)
    center = win.getMouse()
    circumference_pt = win.getMouse()
    radius = math.sqrt(
        center.getX() - circumference_pt.getX()) ** 2 + (center.getY() - circumference_pt.getY()) ** 2
    circle_two = Circle(center, radius)
    circle_two.setFill("light blue")
    circle_two.draw(win)
    overlap_message = Text(Point(2, 6), "the circles overlap!")
    overlap_message.setTextColor("black")
    overlap_message.setSize(10)
    false_message = Text(Point(3, 5), "the circles do not overlap")
    false_message.setTextColor("black")
    false_message.setSize(10)
    close = Text(Point(5, 7), "Click to close")
    close.draw(win)

    if did_overlap(circle_one, circle_two):
        overlap_message.draw(win)
    else:
        false_message.draw(win)
    win.getMouse()
    win.close()


def did_overlap(circle_one, circle_two):
    distance = math.sqrt(math.pow(circle_two.getCenter().getX() - circle_one.getCenter().getX(), 2) +
                         math.pow(circle_two.getCenter().getY() - circle_one.getCenter().getY(), 2))
    if distance <= circle_one.getRadius() + circle_two.getRadius():
        return True
    return False


if __name__ == '__main__':
    pass
