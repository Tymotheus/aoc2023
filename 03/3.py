from string import punctuation, digits
from itertools import chain
punctuation = punctuation.replace(".", "")
# we store the board row wise - [2][4] is third row, 5th value

def parse():
    return open("input.txt").read().splitlines()


class Number:
    value = ""
    starting_cord = [0, 0]

def is_part(value, starting_cord, lookup_symbols):
    ending_cord = [starting_cord[0], starting_cord[1]+len(value)-1]
    if starting_cord[0] == 0: starting_cord[0] = 1
    if starting_cord[0] == 139: starting_cord[0] = 138
    if starting_cord[1] == 0: starting_cord[1] = 1
    if starting_cord[1] == 139: starting_cord[1] = 138
    if ending_cord[1] == 139: ending_cord[1] = 138
    sub_board = lookup_symbols[starting_cord[0]-1:starting_cord[0]+2][starting_cord[1]-1:ending_cord[1]+2] #area of the board surrounding the number
    flat_list = list(chain(*sub_board))
    return True if True in flat_list else False


def solve_first(lines):
    parts = list()
    lookup_symbols = [[True if c in punctuation else False for c in line] for line in lines]
    row_index = 0  # which row we are reading
    for line in lines[:1]:
        column_index = 0  # which column in a row we are reading
        number = ""
        starting_cord = [0, 0]
        scanning = False
        for c in line:
            if scanning:
                if c in digits:
                    number += c
                    if column_index == 139:  # row ends with a number, not with a character
                        if is_part(number, starting_cord, lookup_symbols): parts.append(int(number))
                else:
                    if is_part(number, starting_cord, lookup_symbols): parts.append(int(number))
                    print(number)
                    number = ""
                    starting_cord = [0, 0]  # possible to delete
                    scanning = False
                    column_index += 1
                    continue  # sure its correct?
            elif not scanning:
                if c in digits:
                    scanning = True
                    number = c
                    starting_cord = [row_index, column_index]
            column_index += 1
        row_index += 1
    return sum(parts)



def solve_second(lines):
    pass


print(solve_first(parse()))
print(solve_second(parse()))
