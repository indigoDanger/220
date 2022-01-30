import math

a = int(input('Enter the length of first side: '))
b = int(input('Enter  the length of second side: '))
c = int(input('Enter  the length of third side: '))
def triangle_area(s):
    s = (a + b + c) / 2
    triangle_area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print("The area of the triangle is:", triangle_area)