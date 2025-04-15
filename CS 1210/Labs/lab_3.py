'''
Ben Frederick, Jesse Roberts
CS 1210
Lab 3
'''
import turtle
turtle.shape("turtle")
turtle.color("red")
turtle.speed(12)
def draw_rectangle(x, y ,height, width):
    turtle.penup()
    turtle.setposition(x, y)
    turtle.pendown()
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)


draw_rectangle(0, 0, 140, 200) #draws the main rectangle
draw_rectangle(25, 0, 100, 60) #draws the door

#four window rectangles
draw_rectangle(100, 30, 30, 40)
draw_rectangle(100, 60, 30, 40)
draw_rectangle(140, 30, 30, 40)
draw_rectangle(140, 60, 30, 40)

#draws roof
turtle.penup()
turtle.setposition(0, 140)
turtle.left(45)
turtle.pendown()
turtle.forward(140)
turtle.right(90)
turtle.forward(140)

turtle.left(45)
turtle.penup()
turtle.setposition(-200, -200)
turtle.pendown()

def draw_point(length, angle):
    turtle.forward(length)
    turtle.left(180 - angle)
    turtle.forward(length)

#excersie 3
draw_point(100, 30)
turtle.right(78)
draw_point(100, 30)
turtle.right(78)
draw_point(100, 30)
turtle.right(78)
draw_point(100, 30)
turtle.right(78)
draw_point(100, 30)
turtle.right(78)

#excersie 4
def inner_angle(n , point_angle):
    return (180-point_angle) - (360 / n)

turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))
draw_point(100, 15)
turtle.right(inner_angle(7, 15))

turtle.exitonclick()