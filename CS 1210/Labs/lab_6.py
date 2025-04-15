'''
CS 1210
Ben Frederick, Jesse Roberts, Ethan S
'''

import math

def num_to_digits(n):
    lst = []
    lst.append(n // 100)
    lst.append((n % 100) // 10)
    lst.append(n % 10)
    return lst

def digit_info(n):
    lst0 = num_to_digits(n)
    tp = (min(lst0), max(lst0), sum(lst0))
    return tp

def move(distance, direction, path):
    if not path:
        path.append((0,0))
    current_loc = path[(len(path) - 1)]
    current_x = current_loc[0]
    current_y = current_loc[1]
    d2 = math.radians(direction)
    d_y = distance * math.sin(d2)
    d_x = distance * math.cos(d2)
    new_x = current_x + d_x
    new_y = current_y + d_y
    new_spot = (new_x,new_y)
    path.append(new_spot)
    return path

if __name__ == '__main__':
    n = int(input('Enter an interger: '))
    if n < 1000 and n > 0:
        print(num_to_digits(n))
        print(digit_info(n))
    else:
        print('Integer out of range! Non negative number, less than 1000')
    x = float(input('Enter a side length for an equilateral triangle: '))
    if x > 0:
        path = [(0,0)]
        move(x, 0, path)
        move(x, 120, path)
        move(x, 240, path)
        print(path)