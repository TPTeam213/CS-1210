'''
Ben Frederick
CS 1210
'''

def prime_test(n):
    a = 0
    for i in range(2 , n):
        if (n % i) == 0:
            a += 1
        else:
            pass
    if a == 0:
        return True
    else:
        return False

if __name__ == '__main__':
    num = int(input('Enter an integer > 1: '))
    while num < 1:
        num = int(input('Enter an integer > 1: '))
    if prime_test(num) == True:
        print(f'{num} is prime.')
    else:
        print(f'{num} is not prime.')