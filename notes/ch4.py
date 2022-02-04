from graphics import Entry, Text, Point, GraphWin, Circle
#import math
# win = GraphWin('Face', 700, 700)
# win.setCoords(0, 0, 10, 10)
# face = Circle(Point(5, 6), 3)
# name = Text(Point(5, 1), "Bob")
# name.draw(win)
# user_input = Entry(Point(5, 5), 30)
# user_input.setText("Enter your name: ")
# name = user_input.getText()
# user_input.draw(win)
# print(name)
#
# left_eye = Circle(Point(325, 60), 25)
# left_eye.setFill('yellow')
# left_eye.setOutline('green')
# left_eye.setWidth(10)
# right_eye = left_eye.clone()
# right_eye.move(50, 0)


# print(left_eye.getCenter().getX())
# print(right_eye.getCenter().getX())
# face.draw(win)
# left_eye.draw(win)
# right_eye.draw(win)
#
# click_point = win.getMouse()
# print(click_point.getX(), click_point.getY())

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

#win.setCoords(lowerX of left corner, lowerY of left corner, upperX of right corner, upperY of right corner)
#win.setCoords(0, 0, 10, 10)

#
# def convert():
#     celsius = 10
#     fahrenheit = celsius * 9 / 5 + 32
#     print("the temperature is", fahrenheit, "degrees fahrenheit. Awesome!")
# convert()

def convert_gui():
    win = GraphWin("Converter", 700, 500)
    win.setCoords(0, 0, 10, 10)
    celsius_text = Text(Point(3, 8), "Celsius:")
    celsius_entry = Entry(Point(7, 8), 30)
    click_text = Text(Point(5,5), "Click to Convert")
    result_text = Text(Point(5,1), "")

    celsius_text.draw(win)
    celsius_entry.draw(win)
    click_text.draw(win)
    result_text.draw(win)
    win.getMouse()
    celsius = eval(celsius_entry.getText())
    fahrenheit = celsius * 9 / 5 + 32
    result_text.setText(fahrenheit)
convert_gui()