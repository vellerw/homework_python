from random import choice
import string

def create_str(width):
    s = ''
    for i in range(width):
        c = choice(string.ascii_lowercase + string.ascii_uppercase)
        s += c
    return (s)


def string_(s):
    big = 0
    small = 0
    for c in s:
        if c.isupper():
            big += 1
        else:
            small += 1
        if big > small:
            return 1
        elif big < small:
            return 0
        else:
            return -1


def list_creation(num, s):
    list_ = []
    for i in range(s):
        list_.append(create_str(num))
    return list_


p = list_creation(6, 8)


def percent_creator(s):
    bigger = 0
    smaller = 0
    same_letters = 0
    for x in s:
        if string_(s) == 1:
            bigger += 1
        elif string_(s) == 0:
            smaller += 1
        else:
            same_letters += 1
    ratio_big = (bigger / len(s)) * 100
    ratio_small = (smaller / len(s)) * 100
    ratio_same = (same_letters / len(s)) * 100
    print(ratio_big)
    print(ratio_small)
    print(ratio_same)

print(p)
print(percent_creator(p))
