"""
Name: <Indigo Dockery>
<lab7>.py

Problem: <The program uses the graphics package and practices decision statements to develop a Python program.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import *
import math
from random import randint


def get_random(move_amount):
    return randint(-move_amount, move_amount)


def get_random_color():
    red = randint(0, 255)
    green = randint(0, 255)
    blue = randint(0, 255)
    color = color_rgb(red, green, blue)
    return color


def did_collide(circle_ball, circle_ball2):
    ball_x = circle_ball.getCenter().getX()
    ball2_x = circle_ball2.getCenter().getX()
    ball_y = circle_ball.getCenter().getY()
    ball2_y = circle_ball2.getCenter().getY()

    d = math.sqrt(((ball2_x - ball_x) ** 2) + ((ball2_y - ball_y) ** 2))
    radii1 = circle_ball.getRadius()
    radii2 = circle_ball2.getRadius()
    if d <= (radii1 + radii2):
        return True
    else:
        return False


def hit_vertical(circle_ball, win):
    radius_y = circle_ball.getRadius()
    center_y = circle_ball.getCenter().getY()
    height = win.getHeight()
    bottom = 0
    if (radius_y + center_y) >= height:
        return True
    if (radius_y + center_y) <= bottom:
        return True
    else:
        return False


def hit_horizontal(circle_ball, win):
    radius_x = circle_ball.getRadius()
    center_x = circle_ball.getCenter().getX()
    width = win.getWidth()
    left = 0
    if (radius_x + center_x) >= width:
        return True
    if (radius_x + center_x) <= left:
        return True
    else:
        return False


def bumper():
    # CREATE WINDOW
    win_width = 500
    win_height = 500
    win = GraphWin("Bumper Lab", win_width, win_height)
    win.setBackground("white")
    # CREATE 2 BALLS
    ball1 = randint(10, 400)
    ball1_b = randint(10, 400)
    ball2 = randint(10, 400)
    ball2_b = randint(10, 400)
    circle_ball = Circle(Point(ball1, ball1_b), 10)
    circle_ball2 = Circle(Point(ball2, ball2_b), 10)
    circle_ball.draw(win)
    circle_ball2.draw(win)

    circle_ball.setFill(get_random_color())
    circle_ball2.setFill(get_random_color())

    # USER CLICK TO CLOSE // TIMER // while loop
    x1_direction = get_random(20)
    y1_direction = get_random(20)
    x2_direction = get_random(20)
    y2_direction = get_random(20)
    while not win.checkMouse():
        circle_ball.move(x1_direction, y1_direction)
        circle_ball2.move(x2_direction, y2_direction)
        time.sleep(.25)
        get_random_color()
        if did_collide(circle_ball, circle_ball2):
            x1_direction = -x1_direction
            y1_direction = -y1_direction
            x2_direction = -x2_direction
            y2_direction = -y2_direction
        if hit_vertical(circle_ball, win):
            y1_direction = -y1_direction
        if hit_vertical(circle_ball2, win):
            y2_direction = -y2_direction
        if hit_horizontal(circle_ball, win):
            x1_direction = -x1_direction
        if hit_horizontal(circle_ball2, win):
            x2_direction = -x2_direction
    win.getMouse()
    win.close()


bumper()
