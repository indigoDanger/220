"""
Name: <Indigo Dockery>
<LoopBools>.py

Problem: <This program uses boolean value and decision/ repetition structures to create classes and objects.>

Certification of Authenticity:
<include one of the following>
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""


def fibonacci(n):
    n1, n2 = 1, 1
    pattern = [1, 1, ]
    acc = 0
    if n < 1:
        response = "None"
        return response
    elif n == 1:
        return n1
    else:
        while acc < n:
            nth = n1 + n2
            n1 = n2
            n2 = nth
            acc += 1
            pattern.append(nth)
        return pattern[n - 1]


fibonacci(8)


def double_investment(principle, rate):
    equation = principle
    time = 0
    while equation < 2 * principle:
        equation = equation * (1 + rate)
        time += 1
    return time


def syracuse(n):
    acc = n
    pattern = [n, ]
    while acc != 1:
        if acc % 2 == 0:
            acc = acc / 2
        else:
            acc = 3 * acc + 1
        pattern.append(int(acc))
    return pattern

# def goldbach():
#
