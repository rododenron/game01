import os
import random
import time

def show_field(field, gamer_name, status):
    separator = "  "
    print(" ", *[i for i in range(len(field))], sep=separator)

    for i, line in enumerate(field):
        print(i, *line, sep=separator)

    print(f"Ходит: {gamer_name}. Статус: {status}")
    print("Введите номер строки и столбца через пробел.")


def is_field_full(field):
    if any('-' in i for i in field):
        return False
    return True


def check_field(field, gamer_name):
    if is_field_full(field):
        return 0, "поле заполнено"
    
    for line in field:
        if all([line[0] == i for i in line]) and line[0] != '-':
            return 0, f"выиграл {gamer_name}"
    for i in range(len(field[0])):
        if field[0][i] == field[1][i] == field[2][i] != '-':
            return 0, f"выиграл {gamer_name}"
        
    if field[0][0] == field[1][1] == field[2][2] != '-':
        return 0, f"выиграл {gamer_name}"
    if field[2][0] == field[1][1] == field[0][2] != '-':
        return 0, f"выиграл {gamer_name}"
    return 1, "игра продолжается"


def parse_input(input_string):
    symbols = input_string.split(" ")
    if symbols.__len__() != 2:
        return 0, 0, 1
    if not all([s.isdigit() for s in symbols]):
        return 0, 0, 1
    x = int(symbols[0])
    y = int(symbols[1])
    return x, y, 0


def check_coords(field, x, y):
    if x < 0 or y < 0 or x > len(field[0]) or y > len(field) or field[x][y] != '-':
        return 0
    else:
        return 1


def check_input(field, input_string):
    if input_string == 'x':
        return 0, 0, 0, 0, "игрок завершил игру"

    x, y, error = parse_input(input_string)
    if error:
        return 0, 0, 1, 1, "введены некорректные данные"
    else:
        if check_coords(field, x, y):
            return x, y, 1, 0, "игра продолжается"
        else:
            return 0, 0, 1, 1, "введены неверные координаты"


def action(field , x, y, c):
    field[x][y] = c


def step_robot(field):
    coord_good = 0
    while not coord_good:
        x = random.randint(0, len(field[0]) - 1)
        y = random.randint(0, len(field) - 1)
        coord_good = check_coords(field, x, y)
    print(x, end=" ")
    time.sleep(random.random())
    print(y)
    time.sleep(random.random())
    return x, y, 1, 0, ""


def step_human(field):
    input_string = input()
    return check_input(field, input_string)


if __name__ == '__main__':
    field = [['-' for y in range(3)] for x in range(3)]

    gamer = random.randint(0, 1)
    gamers = [{'gamer_name': 'робот', 'symbol': '0'},
              {'gamer_name': 'человек', 'symbol': 'X'}]

    show_field(field, gamers[gamer]['gamer_name'], "игра началась")
    game_run = 1
    while game_run:
        if gamer:
            x, y, game_run, error, status = step_human(field)
        else:
            x, y, game_run, error, status = step_robot(field)

        os.system('cls' if os.name == 'nt' else 'clear')
        if not error and game_run:
            action(field, x, y, gamers[gamer]['symbol'])
            game_run, status = check_field(field, gamers[gamer]['gamer_name'])
            gamer = 0 if gamer and game_run else 1
        show_field(field, gamers[gamer]['gamer_name'], status)
