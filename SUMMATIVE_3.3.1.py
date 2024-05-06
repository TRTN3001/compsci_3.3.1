import turtle
import tkinter
from tkinter import *
from tkinter import ttk
import random
import pyautogui

# TODO add math "advertisement" where when you die, it makes you solve a polynomial
# TODO make hangman for english as well as other minigames
# TODO make a turtle race

# TKINTER
root = Tk()
root.title("SUMMATIVE 3.3.1")

# VARIABLES
reply = StringVar()
answer = ""

# FUNCTIONS
def submit():
    pass

# OBJECTS
label = Label(root, text="SOLVE A PROBLEM")
entry = Entry(root, textvariable=reply)
submit = Button(root, text="Submit", command=submit)

turtle.done()