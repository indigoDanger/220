"""
Name: <Indigo Dockery>
<Door>.py

Problem: <This program creates a user-defined class and utilizes a list of objects.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
from graphics import*


class Door:

    def __init__(self, shape, label):
        self.shape = shape
        self.text = Text(shape.getCenter(), label)
        self.secret = False

    def get_label(self):
        return self.text.getText()

    def set_label(self, label):
        self.text.setText(label)

    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)

    def undraw(self):
        self.shape.undraw()
        self.text.undraw()

    def is_clicked(self, point):
        corner_point1 = self.shape.getP1()
        corner_point2 = self.shape.getP2()
        x1 = corner_point1.getX()
        y1 = corner_point1.getY()
        x2 = corner_point2.getX()
        y2 = corner_point2.getY()
        if x1 <= point.getX() <= x2 and y1 <= point.getY() <= y2:
            return True
        else:
            return False

    def open(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def close(self, color, label):
        self.color_door(color)
        self.set_label(label)

    def color_door(self, color):
        self.shape.setFill(color)

    def is_secret(self):
        if self.secret:
            return True
        else:
            return False

    def set_secret(self, secret):
        self.secret = secret
