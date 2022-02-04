from graphics import Point, GraphWin, Circle
import math

win = GraphWin('Face', 700, 700)
face = Circle(Point(350, 100), 100)

left_eye = Circle(Point(325, 60), 25)
right_eye = left_eye.clone()
right_eye.move(50, 0)


left_eye.setFill('yellow')
left_eye.setOutline('green')
left_eye.setWidth(10)

# print(left_eye.getCenter().getX())
# print(right_eye.getCenter().getX())
face.draw(win)
left_eye.draw(win)
right_eye.draw(win)

click_point = win.getMouse()
print(click_point.getX(), click_point.getY())


# point_a = Point(50, 70)
# point_b = Point(98, 100)
#
# point_a.move(10, 0)
#
#
# win = GraphWin("CSCI 220", 700, 700)
#
# middle = Point(350, 350)
# middle.draw(win)
#
# my_circle = Circle(middle, 70)
# my_circle.draw(win)
#
#
#
# input("hit enter to exit")
