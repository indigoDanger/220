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


def main():
    playing = True

    win = GraphWin("Test", 500, 500)

    shape = Rectangle(Point(100, 50), Point(300, 100))
    button = Button(shape, "Exit")

    door = Rectangle(Point(100, 150), Point(300, 500))
    label = Door(door, "Closed")
    label.color_door('red')

    button.draw(win)
    label.draw(win)

    while playing:
        click = win.getMouse()
        if label.is_clicked(click):
            if label.get_label() == 'Open':
                label.close('red', 'Closed')
            else:
                label.open('white', 'Open')
        elif button.is_clicked(click):
            playing = not playing

    win.close()


if __name__ == '__main__':
    main()
