'''
Ben Frederick
CS 1210
'''

import random


def roll(n , s):
    c = 0
    for i in range(n):
        c += random.randint(1 , s)
    if c >= 11:
        return True
    else:
        return False


def flips_needed(p):
    coun = 0
    res = ['H', 'T']
    seq = ''
    x = 1
    while x == 1:
        if p in seq:
            x = 0
            return coun
        else:
            seq = seq + str(random.choice(res))
            coun += 1


def first_to_occur(pa, pb):
    res = ['H', 'T']
    seq = ''
    x = 1
    while x == 1:
        if pa in seq:
            x = 0
            return True
        elif pb in seq:
            x = 0
            return False
        else:
            seq = seq + str(random.choice(res))


if __name__ == "__main__":
    #Checking averages for excerise 1
    count = 0
    c2 = 0
    for i in range(100000):
        if roll(1,20):
            count += 1
    for i in range(100000):
        if roll(3,6):
            c2 += 1
    print(f'Average success of one 20-sided die is {count/100000}')
    print(f'Average success of 3 6-sided die is {c2/100000}')

    #Checking averages for excerise 2
    c3 = 0
    c4 = 0
    for i in range(100000):
        c3 += flips_needed('HHT')
    for i in range(100000):
        c4 += flips_needed('THH')
    print(f'The average number of flips needed to find "HHT" is {c3/100000}')
    print(f'The average number of flips needed to find "THH" is {c4/100000}')

    #Checking numbers for excerise 3
    c5 = 0
    c6 = 0
    for i in range(100000):
        if first_to_occur('HHT', 'THH'):
            c5 += 1
        else:
            c6 += 1
    print(f'The average number of times "HHT" was first was {c5/100000}')
    print(f'The average number of times "THH" was first was {c6/100000}')