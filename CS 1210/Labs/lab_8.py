'''
Ben Frederick
CS 1210
'''

import turtle

turtle.speed(10)
turtle.color('red')

def draw_fractal(shape, angle):
    for i in shape:
        if i == 'F':
            turtle.forward(1)
        elif i == '+':
            turtle.left(angle)
        elif i == '-':
            turtle.right(angle)
        else:
            pass

def levy(n):
    shape = '--F'
    new = ''
    for i in range(n):
        for c in shape:
            if c == 'F':
                new = new + '-F++F-'
            elif c == '-':
                new = new + '-'
            elif c == '+':
                new = new + '+'
        shape = new
        new = ''
    return (shape, 45)


def koch(n):
    shape = 'F'
    new = ''
    for i in range(n):
        for c in shape:
            if c == 'F':
                new = new + 'F+F--F+F'
            elif c == '-':
                new = new + '-'
            elif c == '+':
                new = new + '+'
        shape = new
        new = ''
    return (shape, 60)


def sierpinski(n):
    shape = 'XF'
    new = ''
    for i in range(n):
        for c in shape:
            if c == 'X':
                new = new + 'YF+XF+Y'
            elif c == 'Y':
                new = new + 'XF-YF-X'
            elif c == 'F':
                new = new + 'F'
            elif c == '-':
                new = new + '-'
            elif c == '+':
                new = new + '+'
        shape = new
        new = ''
    return (shape, 60)


def dragon(n):
    shape = 'FX'
    new = ''
    for i in range(n):
        for c in shape:
            if c == 'X':
                new = new + 'X+YF+'
            elif c == 'Y':
                new = new + '-FX-Y'
            elif c == 'F':
                new = new + 'F'
            elif c == '-':
                new = new + '-'
            elif c == '+':
                new = new + '+'
        shape = new
        new = ''
    return (shape, 90)


def gosper(n):
    shape = 'XF'
    new = ''
    for i in range(n):
        for c in shape:
            if c == 'X':
                new = new + 'X+YF++YF-FX--FXFX-YF+'
            elif c == 'Y':
                new = new + '-FX+YFYF++YF+FX--FX-Y'
            elif c == 'F':
                new = new + 'F'
            elif c == '-':
                new = new + '-'
            elif c == '+':
                new = new + '+'
        shape = new
        new = ''
    return (shape, 60)

if __name__ == "__main__":
    turtle.shape("turtle")
    turtle.color("green")

    # disables animations
    turtle.tracer(0)

    # changes the coordinate system
    ox, oy = 0, 0
    size = 15
    turtle.setworldcoordinates(ox - size, oy - size, ox + size, oy + size)

    # function testing code
    shape, angle = gosper(2)
    draw_fractal(shape, angle)

    # show drawing and wait to close window
    turtle.update()
    turtle.exitonclick()