def read_data(filename):
    num_list = []
    file = open(filename, "r")
    line = file.readline()
    while line:
        gap = line.split()
        i = 0
        while i < len(gap):
            new_line = eval(gap[i])
            num_list.append(new_line)
            i += 1
        line = file.readline()
    return num_list


def is_in_linear(search_val, values):
    num_list = values
    i = 0
    while i < len(num_list):
        if search_val == num_list[i]:
            return True
        i += 1
    return False
