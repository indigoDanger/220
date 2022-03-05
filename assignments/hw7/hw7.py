"""
Name: <Indigo Dockery>
<hw7>.py

Problem: <This program writes functions, and is capable of reading and writing text files.>

Certification of Authenticity:
I certify that this assignment is my own work, but I discussed it with: Brooke at CSL>
"""
from encryption import *
from encryption import encode_better


def number_words(in_file_name, out_file_name):
    word = open(in_file_name)
    text = word.read()
    outfile = open(out_file_name, "a")
    separate = text.split()
    counter = 1
    for i in separate:
        outfile.write(str(counter) + " " + i + "\n")
        counter = counter + 1
    word.close()
    outfile.close()


def hourly_wages(in_file_name, out_file_name):
    input_file = open(in_file_name)
    output_file = open(out_file_name, "a")
    read_file = input_file.read()
    message = read_file.split("\n")
    for line in message:
        line_split = line.split()
        wage = eval(line_split[2])
        hours = eval(line_split[3])
        pay = (wage * hours) + (1.65 * hours)
        output_file.write(line_split[0] + " " + line_split[1] + " " + pay)
    input_file.close()
    output_file.close()


def calc_check_sum(isbn):
    isbn = isbn.replace("-", "")
    sum_value = 0
    for i in range(10):
        cur_val = eval(isbn[9 - i])
        sum_value += (i + 1) * cur_val
    return sum_value


def send_message(file_name, friend_name):
    file = open(file_name, "r")
    text = file.read()
    write_file = open(friend_name + ".txt", "w")
    write_file.write(text)
    file.close()
    write_file.close()


def send_safe_message(file_name, friend_name, key):
    file = open(file_name)
    text = file.read()
    line = text.split("\n")
    encrypt_file = open(friend_name + ".txt", "w")
    for message in line:
        encrypt_file.write(encode(message, key) + "\n")
    file.close()
    encrypt_file.close()


def send_uncrackable_message(file_name, friend_name, pad_file_name):
    file = open(file_name)
    message_text = file.read()
    key_file = open(pad_file_name)
    key = key_file.read()
    text = message_text.split("\n")
    for i in text:
        encode_better(i, key, friend_name + ".txt")
    file.close()
    key_file.close()


if __name__ == '__main__':
    number_words("pad.txt", "Sammy.txt")
    hourly_wages("pad.txt", "Sammy.txt")
    calc_check_sum("0-072-94652-0")
    send_message("pad.txt", "Sammy")
    send_safe_message("pad.txt", "Sammy", 4)
    send_uncrackable_message("pad.txt", "name", "Sammy.txt")
