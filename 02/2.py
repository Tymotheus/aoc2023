import sys
from string import ascii_letters

lines = open("input.txt").read().splitlines()
board = {"red": 12, "green": 13, "blue": 14}


def solve_first(lines):
    sums = list(range(101))
    counter = 1
    for line in lines:
        draws = line.split(':')[1].split(';')
        for draw in draws:
            for cubes in draw.replace(" ", "").split(","):
                for color in board.keys():
                    if color in cubes and int(cubes.replace(color, "")) > board[color]:
                        sums[counter] = 0
        counter += 1
    return sum(sums)


def solve_second(lines):
    sums = list(range(101))
    counter = 1
    for line in lines:
        minima = {"red": 0, "green": 0, "blue": 0}
        draws = line.split(':')[1].split(';')
        for draw in draws:
            for cubes in draw.replace(" ", "").split(","):
                for color in board.keys():
                    if color in cubes and int(cubes.replace(color, "")) > minima[color]:
                        minima[color] = int(cubes.replace(color, ""))
        sums[counter] = 1*minima["red"]*minima["green"]*minima["blue"]
        counter += 1
    return sum(sums)


print(solve_first(lines))
print(solve_second(lines))
