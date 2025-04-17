'''
Ben Frederick
CS 1210
'''

import csv


if __name__ == '__main__':
    ins = []
    z = 10
    while len(ins) != 10:
        c = 0
        x = input(f'Enter a positive integer ({z} to go): ')
        try:
            x = int(x)
        except ValueError:
            print(f'Cannot convert {x} to an integer!')
            c += 1
        if not c:
            if x < 0:
                print(f'{x} is an integer, but it\'s not positive. Try again.')
            elif x in ins:
                print(f'You already entered {x}!')
            else:
                ins.append(x)
                z -= 1

    n = {}
    k = 1
    with open('staff.csv', 'r') as file:
        r = csv.reader(file)
        for row in r:
            if row[1] in n:
                n[row[1]] += 1
            else:
                n[row[1]] = 1
    hold = 0
    for val in n.values():
        if val > hold:
            hold = val
    
    h = 0
    for key in n:
        if n[key] == hold:
            h = key
    print(f'{h} is the most common first name in staff.csv')