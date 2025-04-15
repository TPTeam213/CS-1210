'''
Ben Frederick
CS 1210
'''

stack = []

i = input('Enter a string, and I\'ll print it backwards! ')


for char in i:
    stack.append(char)


while stack:
    print(stack.pop(), end='')
print()