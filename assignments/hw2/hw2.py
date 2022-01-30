"""
Name: <Indigo Dockery>
<hw2>.py

Problem: <This program the math library to develop simple Python programs that do input, produce output, and do arithmetic.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""
import math

upper_bound = eval(input("what is the upper bound? "))
def sum_of_threes(upper_bound):
    return(sum(range(0, upper_bound+1, 3)))
print("sum of threes is", sum_of_threes(upper_bound))

my_range = range(1, 11)
my_range2 = range(2, 21, 2)  # (start, stop)
my_range3 = range(3, 31, 3)
my_range4 = range(4, 41, 4)
my_range5 = range(5, 51, 5)
my_range6 = range(6, 61, 6)
my_range7 = range(7, 71, 7)
my_range8 = range(8, 81, 8)
my_range9 = range(9, 91, 9)
my_range10 = range(10, 101, 10)
def multiplication_table( ):
    my_range = my_range * 1
    my_range2 = my_range * 1
    my_range3 = my_range * 1
    my_range4 = my_range * 1
    my_range5 = my_range * 1
    my_range6 = my_range * 1
    my_range7 = my_range * 1
    my_range8 = my_range * 1
    my_range9 = my_range * 1
    my_range10 = my_range * 1
print(list(my_range))
print(list(my_range2))
print(list(my_range3))
print(list(my_range4))
print(list(my_range5))
print(list(my_range6))
print(list(my_range7))
print(list(my_range8))
print(list(my_range9))
print(list(my_range10))


a = int(input("Enter side A length: "))
b = int(input("Enter side B length: "))
c = int(input("Enter side C length: "))
s = (a + b + c) / 2
def triangle_area(triangle_area):
    s = s * 1
triangle_area = ((s * (s - a) * (s - b) * (s - c)) ** 0.5)
print("The area of the triangle is:", triangle_area)


start = int(input("Enter the lower range: "))
end = int(input("Enter the upper range: "))
the_range = range(start, end)
def sum_squares(square_numbers):
    the_range = the_range + 1
square_numbers = (the_range * the_range for the_range in the_range)
print(square_numbers)


base = int(input("Enter the base number: "))
exp = int(input("Enter the exponent: "))
def power():
    pass
