from string import punctuation, digits
from itertools import chain
import numpy as np
punctuation = punctuation.replace(".", "")
# we store the board row wise - [2][4] is third row, 5th value

def parse():
    return open("input.txt").read().splitlines()


class Number:
    value = ""
    starting_cord = [0, 0]

def is_part(value, starting_cord, lookup_symbols):
    """A numbers position, is uniquely identifiable by it's starting point and length"""
    ending_cord = [starting_cord[0], starting_cord[1]+len(value)-1]
    if starting_cord[0] == 0: starting_cord[0] = 1
    if starting_cord[0] == 139: starting_cord[0] = 138
    if starting_cord[1] == 0: starting_cord[1] = 1
    if starting_cord[1] == 139: starting_cord[1] = 138
    if ending_cord[1] == 139: ending_cord[1] = 138
    sub_board = lookup_symbols[starting_cord[0]-1:starting_cord[0]+2, starting_cord[1]-1:ending_cord[1]+2] #area of the board surrounding the number
    flat_list = list(chain(*sub_board))
    return True if True in flat_list else False


def in_neighbourhood(value, starting_cord, star: tuple[int, int]):
    """If the star and value are in neighbourhood returns True"""
    print(value)
    print(True if (star[1] >= starting_cord[1]-1 and star[1] <= starting_cord[1]+len(value) and star[0]<=starting_cord[0]+1 and star[0]>=starting_cord[0]-1) else False)
    return True if (star[1] >= starting_cord[1]-1 and star[1] <= starting_cord[1]+len(value) and star[0]<=starting_cord[0]+1 and star[0]>=starting_cord[0]-1) else False


def solve_first(lines):
    parts = list()
    lookup_symbols = [[True if c in punctuation else False for c in line] for line in lines]
    lookup_symbols = np.asarray(lookup_symbols)
    row_index = 0  # which row we are reading
    for line in lines:
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
    # pseudocode: identiy stars -> for every star scan 3 adjacent lines -> if number found, run "in neighbourhood", if True, add to list -> if list has 2 elements, multiply and sum    star_cords = list()
    stars = list()
    for row_index, line in enumerate(lines):
        for column_index, c in enumerate(line):
            if c == '*': stars.append((row_index, column_index))
    gear_ratios = list()
    print(stars)
    for star_row, star_column in stars:
        neighbouring_numbers=list()
        sub_board = lines[max(star_row-1, 0):min(star_row+2, 140)]
        row_index = max(star_row-1,0)  # which row we are reading
        for line in sub_board:
            column_index = 0  # which column in a row we are reading
            number = ""
            starting_cord = [row_index, 0]
            scanning = False
            for c in line:
                if scanning:
                    if c in digits:
                        number += c
                        if column_index == 139:  # row ends with a number, not with a character
                            if in_neighbourhood(number,starting_cord,(star_row,star_column)): neighbouring_numbers.append(number)
                    else:
                        if in_neighbourhood(number,starting_cord,(star_row,star_column)): neighbouring_numbers.append(number)
                        number = ""
                        starting_cord = [row_index, 0]  # possible to delete
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
        if len(neighbouring_numbers) == 2: gear_ratios.append(int(neighbouring_numbers[0])*int(neighbouring_numbers[1]))
    return sum(gear_ratios)

print(solve_first(parse()))
print(solve_second(parse()))
