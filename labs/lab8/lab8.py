"""
Name: <Indigo Dockery>
<lab8>.py

Problem: <This program develops a Python program that uses numeric data from a text file.>

Certification of Authenticity:
I certify that this assignment is entirely my own work.
"""


def weighted_average(in_file_name, out_file_name):
    file = open(in_file_name, "r")
    content = file.readlines()
    write_input = open(out_file_name, "w")
    average = 0
    count = 0
    for line_var in content:
        total_weight = 0
        mult_accum = 0
        split_term = line_var.split(":")
        names = split_term[0]
        numbers = split_term[1]
        num_split = numbers.strip().split(" ")
        for i in range(0, len(num_split), 2):
            weight = eval(num_split[i])
            grade = eval(num_split[i + 1])
            total_weight += weight
            mult_accum += (weight * grade)
        if total_weight < 100:
            response = "Error: The weights are less than 100."
            write_input.write(names + "'s average: " + response + "\n")
        elif total_weight > 100:
            response2 = "Error: The weights are more than 100."
            write_input.write(names + "'s average: " + response2 + "\n")
        else:
            write_input.write(names + "'s average: " + str(mult_accum / 100) + "\n")
            average = average + mult_accum / 100
            count = count + 1

    class_avg = average / count
    write_input.write("class average: " + str(class_avg))
    file.close()
    write_input.close()


if __name__ == '__main__':
    weighted_average("grades.txt", "avg.txt")
