"""
Name: <Indigo Dockery>
<hw5>.py

Problem: <This program uses Python strings and lists, as well as Python indexing and slicing facilities.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
import math


def cash_converter():
    dollar = eval(input("enter an integer: "))
    mystr = "That is ${dollars:.2f}"
    print(mystr.format(dollars=dollar))
def encode():
    message = input("enter a message: ")
    key = eval(input("enter a key: "))
    for i in range(len(message)):
        num_m = ord(message[i])
        letter = chr(num_m + key)
        print(letter, end="")
    print("")
def sphere_area(radius):
    area = (4 * math.pi) * (radius ** 2)
    return area

def sphere_volume(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
def sum_n(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i
    print(sum)

def sum_n_cubes(number):
    sum = 0
    for i in range(1, number + 1):
        sum += i ** 3
    print(sum)
def encode_better():
   phrase = input("enter a message: ")
   key_phrase = input("enter a key: ")
   ret =" "
   for i in range(len(phrase)):
        num_m = ord(phrase[i]) - 65
        num_k = ord(key_phrase[i % len(key_phrase)]) - 65
        number = ((num_m + num_k) % 58) + 65
        cipher_text = chr(number)
        ret+=cipher_text
   print(ret)
if __name__ == '__main__':
    cash_converter()
    encode()
    sphere_area(13)
    sphere_volume(13)
    sum_n(4)
    sum_n_cubes(3)
    encode_better()
