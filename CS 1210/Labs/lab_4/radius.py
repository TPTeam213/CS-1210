'''
Ben Frederick, Jesse Roberts
CS 1210

Program to find the radius of a circle given the area
'''
import math

PI = math.pi

def find_radius(area):
    return math.sqrt((area / PI))

if __name__ == "__main__":
    a = float(input('Enter the area of a circle: '))
    answer = find_radius(a)
    print(f'The radius of the circle is {answer:.2f}')