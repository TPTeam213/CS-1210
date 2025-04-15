'''
Ben Frederick 
CS 1210
'''
#One more time with turtle

import turtle
import time
import random

# up, down, left, right
keys = [False, False, False, False]

def on_press_up():
    keys[0] = True
    print(keys, end = "\r")

def on_release_up():
    keys[0] = False
    print(keys, end = "\r")

def on_press_down():
    keys[1] = True
    print(keys, end = "\r")

def on_release_down():
    keys[1] = False
    print(keys, end = "\r")

def on_press_left():
    keys[2] = True
    print(keys, end = "\r")

def on_release_left():
    keys[2] = False
    print(keys, end = "\r")

def on_press_right():
    keys[3] = True
    print(keys, end = "\r")

def on_release_right():
    keys[3] = False
    print(keys, end = "\r")

def on_click_left(x, y):
    print("left", x, y, end = "\r")

def on_click_right(x, y):
    print("right", x, y, end = "\r")

# disable animations
turtle.tracer(0)

# create player turtle
egbert = turtle.Turtle()
egbert.shape("turtle")
egbert.color("green")
egbert.penup()
turtle.onkeypress(on_press_up, "Up")
turtle.onkeyrelease(on_release_up, "Up")
turtle.onkeypress(on_press_down, "Down")
turtle.onkeyrelease(on_release_down, "Down")
turtle.onkeypress(on_press_left, "Left")
turtle.onkeyrelease(on_release_left, "Left")
turtle.onkeypress(on_press_right, "Right")
turtle.onkeyrelease(on_release_right, "Right")
turtle.onscreenclick(on_click_left)
turtle.onscreenclick(on_click_right, btn = 3)
turtle.listen()
# time of last update
previous = time.time()
locx = random.randint(-250, 250)
locy = random.randint(-250, 250)

writer = turtle.Turtle()
writer.penup()
writer.hideturtle()
writer.setposition(0, 200)
# loop while not game over
while egbert.distance(locx, locy) > 5:
    # check how long it's been since last update
    current = time.time()
    time_step = current - previous
    previous = current
    # update the state based on time_step
    if keys[0] == True:
        egbert.setheading(90)
        egbert.forward(150 * time_step)
    if keys[1] == True:
        egbert.setheading(270)
        egbert.forward(150 * time_step)
    if keys[2] == True:
        egbert.setheading(180)
        egbert.forward(150 * time_step)
    if keys[3] == True:
        egbert.setheading(0)
        egbert.forward(150 * time_step)

    writer.clear()
    z = egbert.distance(locx, locy)
    writer.write(f"Distance: {z}", align="center", font=("Arial", 14, "bold"))
    # draw the updated game state
    turtle.update()

x = locx
y = locy
writer.clear()
writer.write(f"You win! The position was {x} , {y}", align="center", font=("Arial", 14, "bold"))
turtle.update()

turtle.mainloop()