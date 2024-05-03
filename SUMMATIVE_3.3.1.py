from turtle import Turtle, Screen
import tkinter
from tkinter import *
from tkinter import ttk
import random
import pyautogui

# TODO add math "advertisement" where when you die, it makes you solve a polynomial
# TODO make hangman for english as well as other minigames

from turtle import Turtle, Screen

playGround = Screen()

playGround.screensize(250, 250)
playGround.title("Turtle Keys")

run = Turtle("turtle")
run.color("blue")
run.penup()
run.setposition(250, 250)

follow = Turtle("turtle")
follow.color("red")
follow.penup()
follow.setposition(-250, -250)

def k1():
    run.forward(45)

def k2():
    run.left(45)

def k3():
    run.right(45)

def k4():
    run.backward(45)

def quitThis():
    playGround.bye()

def is_collided_with(a, b):
    return abs(a.xcor() - b.xcor()) < 10 and abs(a.ycor() - b.ycor()) < 10

# TODO make faster with 1 second loop
def follow_runner():
    follow.setheading(follow.towards(run))
    follow.forward(min(follow.distance(run), 10))
    if is_collided_with(follow, run):
        print('Collision!')
        quitThis()
    else:
        playGround.ontimer(follow_runner, 10)

playGround.onkey(k1, "Up")  # the up arrow key
playGround.onkey(k2, "Left")  # the left arrow key
playGround.onkey(k3, "Right")  # you get it!
playGround.onkey(k4, "Down")

playGround.listen()

follow_runner()


playGround.mainloop()