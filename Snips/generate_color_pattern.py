#!/bin/python3
'''Generate Symmetrical Random Color art.'''
from random import randint


SCHEMES = {
    '1': ['264653', '2a9d8f', 'e9c46a', 'f4a261', 'e76f51'],
    '2': ['cb997e', 'ddbea9', 'ffe8d6', 'b7b7a4', 'a5a58d', '6b705c'],
    '3': ['03045e', '023e8a', '0077b6', '0096c7', '00b4d8', '48cae4', '90e0ef',
          'ade8f4', 'caf0f8'],
    '4': ['8ecae6', '219ebc', '023047', 'ffb703', 'fb8500']
}


SCHEME_NUM = input(f'Enter scheme number 1\u2013{len(SCHEMES)}: ')


def generate_pattern():
    '''Generate color pattern.'''
    pattern = []

    for _ in range(0, 30):
        scheme = SCHEMES[SCHEME_NUM]
        length = len(scheme)
        rand_num = randint(0, length-1)
        color = scheme[rand_num]
        red = int(color[0:2], 16)
        green = int(color[2:4], 16)
        blue = int(color[4:6], 16)
        pattern.append(f'\x1b[48;2;{red};{green};{blue}m \x1b[0m')

    sym_pattern = ''.join(pattern) + ''.join(pattern[::-1])

    for _ in range(10):
        print(sym_pattern)


if __name__ == '__main__':
    generate_pattern()