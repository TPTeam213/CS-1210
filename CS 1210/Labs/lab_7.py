'''
Ben Frederick
CS 1210
Lab 7
'''

import turtle
turtle.speed(10)
turtle.color('red')

def draw_polygon(n):
    ang = 360 / n
    for i in range(n):
        turtle.forward(100)
        turtle.left(ang)


def draw_star(n, angle):
    in_angle = (180 - angle) - (360 / n)
    for i in range(n):
        turtle.forward(100)
        turtle.left(180 - angle)
        turtle.forward(100)
        turtle.right(in_angle)

def draw_spiral(n):
    lent = 10
    ang = 360 / n
    num = 5 * n
    for i in range(num):
        turtle.forward(lent)
        turtle.left(ang)
        lent += 10

if __name__ == '__main__':
    draw_polygon(8)
    turtle.penup()
    turtle.setposition(-200, -200)
    turtle.pendown()
    draw_star(7,15)
    turtle.penup()
    turtle.setposition(-200, 300)
    turtle.pendown()
    draw_spiral(6)
    turtle.exitonclick()