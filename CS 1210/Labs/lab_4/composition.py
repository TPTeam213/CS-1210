'''
Ben Frederick, Jesse Roberts
CS 1210

Program to perform function composition
'''

def f(x):
    return x ** 2

def g(x):
    return x + 5

if __name__ == '__main__':
    x = int(input('Enter a value for x: '))
    f_of_g = f(g(x))
    g_of_f = g(f(x))
    print(f'f(g({x})) = {f_of_g}, and g(f(x)) = {g_of_f}')