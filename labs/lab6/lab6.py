from graphics import *
def vigenere():
    #create window
    win_width = 400
    win_height = 400
    win = GraphWin("Vigenere Lab", win_width, win_height)
    win.setBackground("white")

    #creating boxes
    message = Entry(Point(250, 100), 30)
    keyword = Entry(Point(250, 150), 20)
    encode = Rectangle(Point(200, 200), Point(276, 250))
    text = Text(Point(238, 225), "Encode")
    text.draw(win)

    # create text instructions
    msg = Text(Point(75, 100), "Message to code")
    msg.draw(win)
    kywrd = Text(Point(100, 150), "Enter Keyword")
    kywrd.draw(win)

    #drawing boxes
    message.draw(win)
    keyword.draw(win)
    encode.draw(win)

    win.getMouse()

    #pull text from box
    text = message.getText().upper().replace(" ", "")
    key = keyword.getText().upper().replace(" ", "")

    x = " "

    for i in range(len(text)):
        num_m = ord(text[i]) - 65
        print(num_m, end=" ")
        num_k = ord(key[i % len(key)]) - 65
        print(num_k, end=" ")
        number = (num_m + num_k)%26
        letter_m = chr(number + 65)
        #concat to empty string
        x = x + letter_m
    #print resulting message
    result = Text(Point(200, 350), x)
    result.draw(win)

    #click to close
    bye = Text(Point(200, 375), "Click again to close")
    bye.setTextColor("black")
    bye.draw(win)
    win.getMouse()
    win.close()


vigenere()


