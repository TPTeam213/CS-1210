'''
Lab 5
Ben Frederick and Jesse Roberts
CS 1210
'''


def rightmost_positive(n):
    if n <= 9:
        return n
    else:
        return n % 10


def rightmost(n):
    if n > 0:
        return n % 10
    else:
        return int((n / -1)) % 10


def second_from_the_right(n):
    if n < 0:
        return int(((n / -1) // 10) % 10)
    else:
        return (n // 10) % 10


def repeating_digits(n):
    return n + (n * 11) + (n * 111)


if __name__ == '__main__':
    n1 = int(input('Enter a positive integer: '))
    if n1 > 0:
        print(f'The rightmost digit is: {rightmost_positive(n1)}') 
    else:
        print(f'{n1} is not positive!')
    n2 = int(input('Enter an integer: '))
    print(f'The rightmost digit is {rightmost(n2)}')
    n3 = int(input('Enter an integer: '))
    if n3 <= 9 and n3 >= -9:
        print('Not enough digits!')
    else:
        print(f'The second digit from the right is: {second_from_the_right(n3)}')
    n4 = int(input('Enter an integer in the range [0, 9]: '))
    if n4 >= 0 and n4 <= 9:
        print(f'The result is: {repeating_digits(n4)}')
    else:
        print('Invalid input')