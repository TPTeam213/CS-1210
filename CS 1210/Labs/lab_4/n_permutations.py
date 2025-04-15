'''
Ben Frederick, Jesse Roberts
CS 1210


'''

import math

def permute(n, r):
    return math.factorial(n) // (math.factorial((n - r)))

if __name__ == "__main__":
    n = int(input('Enter a value for n, the number of elements in the set: '))
    r = int(input('Enter the number of elements chosen, r: '))
    perms = permute(n, r)
    print(f'There are {perms:,} r-permutations, given n = {n} and r = {r}')