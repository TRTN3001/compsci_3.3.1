import turtle
import tkinter
from tkinter import *
from tkinter import ttk
import random
import pyautogui

# TODO add math "advertisement" where when you die, it makes you solve a polynomial
# TODO make hangman for english as well as other minigames
# TODO make a turtle race

# Tkinter
root = Tk()
root.title("SUMMATIVE 3.3.1")
root.geometry("250x200")

# Ensures user can't close window
def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)

# Variables
reply = StringVar()
answer = ""
pquestion = ["2x\u00b2+3x+1", "x\u00b2−5x+6", "3x\u00b2+4𝑥+1", "x\u00b2+6x+9"]
panswer = ["(2x+1)(x+1)", "(x−2)(x−3)", "(3x+1)(x+1)", "(x+3)(x+3)"]
question = random.randint(1,4)

# Functions
def roll():
    question = random.randint(1,4)
    label.config(text="YOUR CATEGORY: POLYNOMIALS!")
    root.after(1000,label.config(text="SOLVE THIS POLYNOMIAL: " + pquestion[(question - 1)]))

def submit():
    if reply.get() == panswer[(question - 1)]:
        label.config(text="CORRECT! NEXT QUESTION IN 3 SECONDS...")
    else:
        label.config(text="INCORRECT! NEXT QUESTION IN 3 SECONDS...")
        root.after(3000, root.destroy())
    root.after(3000, roll)
    submit_button.config(text="Start", command=start)

def start():
    roll()
    submit_button.config(text="Submit", command=submit)

# Objects
label = Label(root, text="SOLVE A PROBLEM")
entry = Entry(root, textvariable=reply)
submit_button = Button(root, text="Start", command=start)

# Packing items (displays on screen)
to_pack = [label, entry, submit_button]
for item in to_pack:
    item.pack()

# Mainloops
# NOTE: DO NOT PUT ANY CODE AFTER THIS
root.mainloop()
turtle.done()