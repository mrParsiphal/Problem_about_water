import random


test_list = [1, 2, 3, 4, 8, 7, 6, 5]
info = True


def Rand(spisok):
    random.shuffle(spisok)


def Grafik(spisok, x=-1, y=-1, check = False, stop = False):
    spisok_length = len(spisok)
    print('<', '-' * spisok_length * 2, '>', sep='')
    height = max(spisok)
    for line in range(height, 0, -1):
        spisok_line = ''
        for stolb in range(spisok_length):
            if x != -1:
                if (line == y) and (stolb == x):
                    if stop == True:
                        spisok_line += '{}'
                    else:
                        spisok_line += '()'
                else:
                    if spisok[stolb] >= line:
                        spisok_line += '[]'
                    elif (check == True) and (stolb == x) and (line < y):
                        spisok_line += '!!'
                    else:
                        spisok_line += '::'
            else:
                if spisok[stolb] >= line:
                    spisok_line += '[]'
                else:
                    spisok_line += '::'

        print(' ', spisok_line, ' ', line, sep='')
    print(' ', end='')
    t = 0
    for value in range(1, spisok_length + 1):
        print(f'{value}'.ljust(2, ' '), end='')
        t += 1
    print()
    print('<', '-' * spisok_length * 2, '>', sep='')


def Zalito(spisok, info):
    print('Random test list: ', spisok)
    height = max(spisok)
    counter = [0 for _ in range(height)]
    cursor = spisok[0]
    if info == True:
        print(end='\n')
        print('program info:')
        print('Initial values:')
        print('*' * (len(spisok) + 17))
        print('height =', height)
        print('cursor value =', cursor)
        Grafik(spisok, 0, cursor, False, True)
        print('*' * (len(spisok) + 17))
    total_amount = 0
    spisok_length = len(spisok)
    for stolbec in range(1, spisok_length):
        check = False
        stop = False
        if info == True:
            print(end='\n')
            print('Cicle #', stolbec)
            print('*' * (len(spisok) + 17))
            print('column =', stolbec + 1)
            print('column value =', spisok[stolbec])
        if cursor > spisok[stolbec]:
            check = True
            for position in range(spisok[stolbec], cursor):
                counter[position] += 1
            for position in range(spisok[stolbec]):
                total_amount += counter[position]
                counter[position] = 0
        elif cursor == spisok[stolbec]:
            stop = True
            for position in range(cursor):
                total_amount += counter[position]
                counter[position] = 0
        else: # cursor < spisok[stolbec]
            stop = True
            cursor = spisok[stolbec]
            for position in range(cursor):
                total_amount += counter[position]
                counter[position] = 0
        if info == True:
            Grafik(spisok, stolbec, cursor, check, stop)
            print('cursor value =', cursor)
            print('total amount = ', total_amount)
            print('counters volume =', counter)
            print('*' * (len(spisok) + 17))
    return total_amount



if __name__ == '__main__':
    Rand(test_list)
    Grafik(test_list)
    print('result =', Zalito(test_list, info))
    input('Press enter')

