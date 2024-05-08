import turtle
import tkinter
from tkinter import *
from tkinter import ttk
import random

# Button config options if OS is Mac
import platform
if platform.system() == "Darwin":
    from tkmacosx import Button # type: ignore
    

# NOTE Turtle
redwin = 0
bluewin = 0

canvas = turtle.Screen()

# Red Turtle
turtle.red = turtle.Turtle("turtle")
turtle.red.color("red")
turtle.red.penup()
turtle.red.setposition(-300, 50)

# Blue Turtle
turtle.blue = turtle.Turtle("turtle")
turtle.blue.color("blue")
turtle.blue.penup()
turtle.blue.setposition(-300, -50)

# Finish Line
turtle.finish = turtle.Turtle()
turtle.finish.color("black")
turtle.finish.penup()

# Functions
def draw_finish():
    turtle.finish.setposition(300, 300)
    turtle.finish.pendown()
    turtle.finish.pensize(10)
    turtle.finish.right(90)
    turtle.finish.forward(600)

# Start functions
draw_finish()


# TODO make hangman for english as well as other minigames
# TODO make a turtle race


# NOTE Tkinter
root = Tk()
root.title("SUMMATIVE 3.3.1")  # TODO change title to something more fitting
root.geometry("275x200")

# Ensures user can't close window
def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)

# Variables
# NOTE "\u00b" is the unicode replacement character for a squared symbol
userInput = StringVar(root)
pquestion = ["2x\u00b2+3x+1", "x\u00b2-5x+6", "3x\u00b2+4x+1", "x\u00b2+6x+9", "x\u00b2-9", "4x\u00b2-4x-3", "x\u00b2+5x+6", "2x\u00b2+7x+3", "3x\u00b2-5x-2", "2x\u00b2-9x+9"]
panswer = ["(2x+1)(x+1)", "(x-2)(x-3)", "(3x+1)(x+1)", "(x+3)(x+3)", "(x-3)(x+3)", "(2x-3)(2x+1)", "(x+2)(x+3)", "(2x+1)(x+3)", "(3x+1)(x-2)", "(2x-3)(x-3)"]

# Functions
def roll():
    global question
    question = random.randint(1,10)
    label.config(text="SOLVE THIS POLYNOMIAL: " + pquestion[(question - 1)])
    entry.delete(0, 'end')

def submit():
    global redwin, bluewin
    if userInput.get() == panswer[(question - 1)]:
        label.config(text="CORRECT! YOU MOVE FORWARD!")
        turtle.blue.forward(50)
        bluewin += 1
    else:
        label.config(text="INCORRECT! RED MOVES FORWARD!")
        turtle.red.forward(60)
        redwin += 1
    checkWin()

def checkWin():
    if bluewin == 12 or redwin == 10:
        if bluewin == 12:
            label.config(text="BLUE WINS! GAME STARTS IN 5 SECONDS")
        if redwin == 10:
            label.config(text="RED WINS! GAME STARTS IN 5 SECONDS")
        root.protocol("WM_DELETE_WINDOW", close)
        root.after(5000, playAgain)
    else:
        root.after(3000, roll)

def playAgain():
    global bluewin, redwin
    bluewin = 0
    redwin = 0
    turtle.blue.setposition(-300, -50)
    turtle.red.setposition(-300, 50)
    submit_button.DISABLED = False
    root.protocol("WM_DELETE_WINDOW", disable_event)
    roll()

def close():
    root.destroy()
    canvas.bye()

# Objects
label = Label(root, text="", font="TkFixedFont", padx=5, pady=5)
entry = Entry(root, textvariable=userInput, font="TkFixedFont")
submit_button = Button(root, text="Submit", command=submit, font="TkFixedFont")
# Packing items (displays on screen)
to_pack = [label, entry, submit_button]
for item in to_pack:
    item.pack()

# Start functions
roll()

# Mainloops
# NOTE: DO NOT PUT ANY CODE AFTER THIS
root.mainloop()
