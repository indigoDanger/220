# def my_first_while():
#     for i in range(5):
#         print(i, end=" ")
#         print('\n{0: < 70}'.format())
#         i = 0
#         while i < 5:
#             print(i, end=" ")
#             i = i + 1
#         print()
#         print(i)
#

# my_first_while()


def is_game_over(player_one_points, player_two_points):
    over_fifteen = player_one_points >= 15 or player_two_points >= 15
    won_by_two = abs(player_one_points - player_two_points) >= 2
    skunked = player_one_points >= 7 and player_two_points <= 0 or player_two_points >= 7 and player_one_points <= 0
    if over_fifteen and won_by_two or skunked:
        return True
    return False


def deMorgan_two(a, b):
    return not(a and b) == (not a or not b)

def deMorgan_test():
    tests = [[True, True], [True, False], [False, True], [False, False]]
    for test in tests:
        # test = the first element of the list [True, True]
        a = test[0]
        b = test[1]
        result = deMorgan_two(a, b)
        print('input: {}, output: {}'.format(test, result))


if __name__ == '__main__':
    player_1 = 0
    player_2 = 0
    print(player_1, player_2)
    while True:
        one_points, two_points = eval(input('enter points for player 1 and 2: '))
        player_1 = player_1  + one_points
        player_2 = player_2 + two_points
        print(player_1, player_2)
        if is_game_over(player_1, player_2):
            break
    print('GAME OVER!')


def average_sentinel():
    acc = 0
    count = 0
    num = 0
    while num >= 0:
        num = eval(input('enter a number (enter a negative number)>> '))
        acc = acc + num
        count = count + 1
    print('average: {} '.format(acc / count))
