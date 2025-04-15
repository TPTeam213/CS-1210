'''
Ben Frederick
CS 1210
'''

def absolute(x):
    if x >= 0:
        return x
    elif x < 0:
        return -(x)

def sgn(x):
    if x > 0:
        return 1
    elif x == 0:
        return x
    else:
        return -1

def tri(x):
    if absolute(x) < 1:
        return 1 - absolute(x)
    else:
        return 0

def relu(x):
    if x >= 0:
        return x
    else:
        return 0
    
def leaky_relu(x, alpha):
    if x >= 0:
        return x
    else:
        return x * alpha