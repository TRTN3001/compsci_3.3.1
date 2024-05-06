import turtle
import tkinter
from tkinter import *
from tkinter import ttk
import random

# Button config options if OS is Mac
import platform
if platform.system() == "Darwin":
    from tkmacosx import Button

# TODO add math "advertisement" where when you die, it makes you solve a polynomial
# TODO make hangman for english as well as other minigames
# TODO make a turtle race

canvas = turtle.Screen()

# Tkinter
root = Tk()
root.title("SUMMATIVE 3.3.1")
root.geometry("275x200")

# Ensures user can't close window
def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)

# Variables
reply = StringVar()
question = random.randint(1,4)
pquestion = ["2x\u00b2+3x+1", "x\u00b2−5x+6", "3x\u00b2+4x+1", "x\u00b2+6x+9"]
panswer = ["(2x+1)(x+1)", "(x−2)(x−3)", "(3x+1)(x+1)", "(x+3)(x+3)"]

# Functions
def roll():
    global question, pquestion
    question = random.randint(1,4)
    label.config(text="SOLVE THIS POLYNOMIAL: " + str(pquestion[(question - 1)]))

def submit():
    global question, panswer, reply
    if str(reply.get()) == str(panswer[(question - 1)]):
        label.config(text="CORRECT! NEXT QUESTION IN 3 SECONDS")
        root.after(3000, roll)
    else:
        label.config(text="INCORRECT! DELETING IN 3 SECONDS")
        root.after(3000, quit)

def quit():
    root.destroy()
    canvas.bye()
# Objects
label = Label(root, text="")
entry = Entry(root, textvariable=reply)
submit_button = Button(root, text="Submit", command=submit)

# Packing items (displays on screen)
to_pack = [label, entry, submit_button]
for item in to_pack:
    item.pack()

# Start functions
roll()

# Mainloops
# NOTE: DO NOT PUT ANY CODE AFTER THIS
root.mainloop()