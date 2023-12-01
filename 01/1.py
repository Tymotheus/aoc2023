import sys
from string import ascii_letters

lines = open("input.txt").read().splitlines()


d = {"one": 'o1e', "two":'t2o',"three":"t3e","four":"4","five":"5e","six":"6","seven":"7n","eight":"e8t","nine":"n9e"}


def solve_first():
    s = 0
    for line in lines:
        line = line.strip(ascii_letters)
        s += int(line[0] + line[-1])
    return s

def solve_second():
    s = 0
    for line in lines:
        l = line
        for k in d.keys():
            l = l.replace(k, d[k])
        l = l.strip(ascii_letters)
        s += int(l[0] + l[-1])
    return s

print(solve_first())
print(solve_second())
