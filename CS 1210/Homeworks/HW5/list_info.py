'''
Ben Frederick
CS 1210
'''

DATA = [15, 16, 3, 17, 6, 8, 19, 12, 16, 5, 24, 16, 18, 14, 7, 12, 6, 2, 5, 16]

def mean(lst):
    return (sum(lst)) / (len(lst))

if __name__ == '__main__':
    x = int(input('Enter an index from 0 to 19 (inclusive): '))
    if x <= 19 and x >= 0:
        print(f'The element at index {x} is {DATA[x]}.')
        print(f'The sum of elements in DATA is {sum(DATA)}.')
        print(f'The largest value in DATA is {max(DATA)}.')
        print(f'The smallest value in DATA is {min(DATA)}.')
        print(f'DATA has {len(DATA)} elements.')
        print(f'The mean of elements in DATA is {mean(DATA)}.')
    else:
        print('Invalid input')