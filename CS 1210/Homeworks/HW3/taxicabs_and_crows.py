'''
Ben Frederick
CS 1210
'''
import math
STRTS_PER_MILE = (1/20)
AVNS_PER_MILE = (1/7)

def taxicab_distance(streets, avenues):
    street_distance = streets * STRTS_PER_MILE
    avenue_distance = avenues * AVNS_PER_MILE
    return street_distance + avenue_distance

def crow_distance(streets, avenues):
    a = streets * STRTS_PER_MILE
    b = avenues * AVNS_PER_MILE
    a = a ** 2
    b = b ** 2
    c = a + b
    c = math.sqrt(c)
    return c

if __name__ == '__main__':
    streets = int(input('How many street blocks must you travel? '))
    avenues = int(input('How many avenue blocks must you travel? '))
    crow_distance(streets, avenues)
    num = taxicab_distance(streets, avenues) - crow_distance(streets, avenues)
    print(f'The crow\'s flight is {num:.2f} miles shorter.')