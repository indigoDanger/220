"""
Name: <Indigo Dockery>
<hw3>.py

Problem: <This program requests input, produces output, and does arithmetic using for loops.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with Brookes at CSS: <Name(s)>
"""

def average():
    num_grades = eval(input("how many grades will you enter? "))
    grade_avg = 0
    for _ in range(num_grades):
        avg = eval(input("Enter grade: "))
        grade_avg = grade_avg + (avg / num_grades)
    print(grade_avg)

def tip_jar():
    tips = 0
    for i in range(5):
        ques = eval(input("how much would you like to donate? "))
        tips = tips + ques
    print("total tips:", tips)


def newton():
    square_root = eval(input("What number do you want to square root? "))
    num_times = eval(input("How many times should we improve the approximation? "))
    approx = square_root
    for i in range(num_times):
        approx = (approx + (square_root / approx)) / 2
    print(approx)

def sequence():
    num_terms = eval(input("how many terms would you like? "))
    output = ("")
    for j in range(num_terms):
        output = output + str(j + ((j - 1)%2)) + (" ")
    print(output)


def pi():
    n = eval(input("how many terms in the series? "))
    product = 1
    for i in range(n):
        numer = ((i -1)%2)+i+1
        denom = i + (i%2)+1
        product = (product * numer / denom)
    print(product * 2)



if __name__ == '__main__':
    pass
