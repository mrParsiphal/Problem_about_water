import random
from format_text import Fat, Blue, Black, Yellow, Green, Red, Violet, Italic

a = [1, 2, 3, 4, 8, 7, 6, 5]
b = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 4, 3, 2, 3, 8, 11, 4, 2, 4, 2, 3, 8, 10, 7, 1, 5, 6, 9]
c = [4, 2, 3, 8, 10, 7, 1, 5, 6, 9]
info = False


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
                        spisok_line += Fat(Red('[]'))
                    else:
                        spisok_line += Fat(Violet('[]'))
                else:
                    if spisok[stolb] >= line:
                        if stolb % 2 == 0:
                            spisok_line += Fat(Yellow('[]'))
                        else:
                            spisok_line += Fat(Green('[]'))
                    elif (check == True) and (stolb == x) and (line < y):
                        spisok_line += Blue('[]')
                    else:
                        spisok_line += Black('[]')
            else:
                if spisok[stolb] >= line:
                    if stolb % 2 == 0:
                        spisok_line += Fat(Yellow('[]'))
                    else:
                        spisok_line += Fat(Green('[]'))
                else:
                    spisok_line += Black('[]')

        print(' ', Fat(spisok_line), ' ', line, sep='')
    print(' ', end='')
    t = 0
    for value in range(1, spisok_length + 1):
        if t % 2 == 0:
            print(Yellow(f'{value}'.ljust(2, ' ')), end='')
        else:
            print(Green(f'{value}'.ljust(2, ' ')), end='')
        t += 1
    print()
    print('<', '-' * spisok_length * 2, '>', sep='')


def Zalito(spisok, info):
    print('Random test list', spisok)
    height = max(spisok)
    counter = [0 for _ in range(height)]
    cursor = spisok[0]
    if info == True:
        print(end='\n')
        print(Italic('initialization program:'))
        print(Fat('Cicle #0'))
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
            print(Fat('Cicle #'), stolbec)
            print('*' * (len(spisok) + 17))
            print('stolbec =', stolbec + 1)
            print('stolbec value =', spisok[stolbec])
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
            print('total_amount = ', total_amount)
            print(counter)
            print('*' * (len(spisok) + 17))
    return total_amount



if __name__ == '__main__':
    Rand(a)
    Grafik(a)
    print('result =', Zalito(a, info))
    input('Press enter')

