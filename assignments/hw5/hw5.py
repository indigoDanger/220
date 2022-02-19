"""
Name: <Indigo Dockery>
<hw5>.py

Problem: <This program uses Python strings and lists, as well as Python indexing and slicing facilities.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""


def name_reverse():
    name = input("enter a name ")
    x = name.split()
    first = x[0]
    last = x[1]
    print(last, first)

def company_name():
    company = input("enter company name with a three part domain: ")
    word = company.split(".")
    print(word[1], end=" ")

def initials():
    num_students = int(input("enter the number of students in the class:"))
    for i in range(num_students):
        first = input("enter students first name: ")
        last = input("enter the students last name: ")
        print("initials: ", first[0] + last[0])

# def names():
#     name_list = eval(input("enter a list of names: "))
#     initial = 0
#     for i in range(name_list):
#         initial = name_list.split(".")
#     print(initial[0], initial[1], initial[2], initial[3], initial[4], initial[5])

def thirds():
    num = eval(input("enter the number of sentences: "))
    sentence = []
    for i in range(num):
        sen = input("enter sentence" + str(i+1) + ":")
        sentence.append(sen)
    for i in sentence:
        output = ""
        for j in range(0, len(i), 3):
            output = output + i[j:j+1]
        print(output)
        output = ""

def word_average():
    sum = 0
    words = input("enter a sentence:")
    x = words.split()
    num = len(x)
    for i in x:
        sum = sum + len(i)
    avg = sum / num
    print(avg)

def pig_latin():
    sentence = input("enter a sentence to convert to pig latin: ")
    word = sentence.split()
    new = ""
    for i in word:
        new += i[1:]+i[0]+"ay "
        new = new.lower()
        new = new.capitalize()
    print(new)

if __name__ == '__main__':
    name_reverse()
    initials()
    #names() - doesn't run
    thirds()
    word_average()
    pig_latin()
