'''
Ben Frederick
CS 1210
'''

import math
PI = math.pi

def slant_height(radius, height):
    x = (radius ** 2) + (height ** 2)
    return math.sqrt(x)


def surface_area(radius, height):
    return (PI * (radius ** 2 )) + (PI * radius * slant_height(radius, height))


def volume(radius, height):
    return (1/3) * PI * (radius ** 2) * height


if __name__ == '__main__':
    radius = float(input('Enter radius: '))
    height = float(input('Enter height: '))
    print(f'Volume: {volume(radius, height):,.2f} units cubed.')
    print(f'Surface area: {surface_area(radius, height):,.2f} units squared.')