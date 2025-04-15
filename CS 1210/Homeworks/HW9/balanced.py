'''
Ben Frederick
CS 1210
'''

def balanced(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if len(stack) == 0 or stack.pop() != '(':
                return False
    return len(stack) == 0

if __name__ == '__main__':
    i = input('Enter a string containing parentheses: ')
    if balanced(i):
        print('Parentheses are balanced!')
    else:
        print('Parentheses are not balanced!')