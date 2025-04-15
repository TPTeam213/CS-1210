'''
Ben Frederick, Jesse Roberts
CS 1210

Program to determine the new time after several hours have elapsed.
'''

def fast_forward(time, duration):
    return (time + duration) % 12

if __name__ == "__main__":
    t = int(input('Enter the current hour [0 - 11]: '))
    d = int(input('Enter the duration (any positive int): '))
    new_time = fast_forward(t, d)
    print(f'After {d} hours(s), the clock will read {new_time} hours(s)')