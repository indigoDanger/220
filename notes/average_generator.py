def average_sentinel():
    acc = 0
    count = 0
    num = eval(input('enter a number (enter a negative number to stop)>> '))
    while num >= 0:
        acc = acc + num
        count = count + 1
        num = eval(input('enter a number (enter a negative number to stop)>> '))
    print('average: {} '.format(acc / count))


def average_sentinel_enter():
    acc = 0
    count = 0
    num = input('enter a number (enter to stop)>> ')
    while num != '':
        acc = acc + eval(num)
        count = count + 1
        num = eval(input('enter a number (enter to stop)>> '))
    print('average: {} '.format(acc / count))


def average_file():
    acc = 0
    count = 0
    file_name = 'file_data.txt'
    file = open(file_name, 'r')
    line = file.readline()
    while line != '':
        #line = '4,5,6'
        num_string = line.split(',') # ['4', '5', '6']
        i = 0
        while i < len(num_string):
            acc = acc + eval(num_string[i])
            count = count + 1
            i = i + 1
            line = file.readline()
    print('average: {}'.format(acc / count))

