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
turtle.title("TURTLE TRAINER 3000")

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


# NOTE Tkinter
root = Tk()
root.title("TURTLE TRAINER 3000")
root.geometry("275x225")
root.config(bg="#323232")

# Ensures user can't close window
def disable_event():
    pass
root.protocol("WM_DELETE_WINDOW", disable_event)

# Variables
# NOTE "\u00b" is the unicode replacement character for a squared symbol
userInput = StringVar(root)
pquestion = ["2x\u00b2+3x+1", "x\u00b2-5x+6", "3x\u00b2+4x+1", "x\u00b2+6x+9", "x\u00b2-9", "4x\u00b2-4x-3", "x\u00b2+5x+6", "2x\u00b2+7x+3", "3x\u00b2-5x-2", "2x\u00b2-9x+9"]
panswer = ["(2x+1)(x+1)", "(x-2)(x-3)", "(3x+1)(x+1)", "(x+3)(x+3)", "(x-3)(x+3)", "(2x-3)(2x+1)", "(x+2)(x+3)", "(2x+1)(x+3)", "(3x+1)(x-2)", "(2x-3)(x-3)"]
turtle_affirmation = ['"I believe in you! You got this!"', '"You think you can do it?"', '"This is it! You can do it!"', '"Just a few more! Push through!"', '"Would Mr. Larson be proud of you?"', '"Shell yeah! Keep on rocking!"', '"TRTN? More like TRTL."', '"ScubaFishy? More like ScubaTurtle."', '"Feel the Shellborne Suffering!"', '"This looks like wishful thinking."']

# Functions
def roll():
    global category, question, r1
    category = random.randint(1, 6)
    turtle_num = random.randint(1, 10)
    if category == 1:  # Polynomials
        question = random.randint(1, 10)
        label.config(text="SOLVE THIS POLYNOMIAL: " + pquestion[(question - 1)])
    elif category == 2:  # Addition
        q1 = random.randint(-100, 1000)
        q2 = random.randint(-100, 1000)
        r1 = q1 + q2
        label.config(text="WHAT IS " + str(q1) + (" + ") + str(q2) + "?")
    elif category == 3:  # Subtraction
        q1 = random.randint(-100, 1000)
        q2 = random.randint(-100, 1000)
        r1 = q1 - q2
        label.config(text="WHAT IS " + str(q1) + (" - ") + str(q2) + "?")
    elif category == 4:  # Multiplication
        q1 = random.randint(-10, 20)
        q2 = random.randint(-10, 20)
        r1 = q1 * q2
        label.config(text="WHAT IS " + str(q1) + (" X ") + str(q2) + "?")
    elif category == 5:  # Division
        q1 = random.randint(1, 30)
        q2 = random.randint(1, 30)
        r1 = q1 * q2
        label.config(text="WHAT IS " + str(r1) + (" / ") + str(q2) + "?")
        r1 = q1
    elif category == 6:  # Algebra
        q1 = random.randint(1, 30)
        q2 = random.randint(1, 30)
        r1 = q1 * q2
        label.config(text="SOLVE FOR X: " + str(r1) + ("x = ") + str(q2))
        r1 = q1
    turtle_text.config(text=turtle_affirmation[(turtle_num - 1)])

def submit():
    global redwin, bluewin
    if category == 1:  # If category is polynomials:
        if userInput.get() == panswer[(question - 1)]:
            label.config(text="CORRECT! YOU MOVE FORWARD!")
            turtle_text.config(text='"Great job! Keep it up :)"')
            turtle.blue.forward(50)
            bluewin += 1
        else:
            label.config(text="INCORRECT! RED MOVES FORWARD!")
            turtle_text.config(text='"Aw, man! The answer was ' + panswer[(question - 1)] + '"')
            turtle.red.forward(60)
            redwin += 1
    elif category == 2 or 3 or 4 or 5 or 6:  # If category is addition, subtraction, multiplication, or division:
        if userInput.get() == str(r1):
            label.config(text="CORRECT! YOU MOVE FORWARD!")
            turtle_text.config(text='"Great job! Keep it up :)"')
            turtle.blue.forward(50)
            bluewin += 1
        else:
            label.config(text="INCORRECT! RED MOVES FORWARD!")
            turtle_text.config(text='"Aw, man! The answer was ' + str(r1) + '"')
            turtle.red.forward(60)
            redwin += 1
    entry.delete(0, 'end')
    checkWin()

def checkWin():
    if bluewin == 12 or redwin == 10:  # Check if turtle reached the end
        if bluewin == 12:
            label.config(text="BLUE WINS! GAME STARTS IN 10 SECONDS")
        if redwin == 10:
            label.config(text="RED WINS! GAME STARTS IN 10 SECONDS")
        turtle_text.config(text='"You can quit now, or keep training!"')
        root.protocol("WM_DELETE_WINDOW", close)
        submit_button.DISABLED = True
        root.after(10000, playAgain)
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
label = Label(root, text="", font="TkFixedFont", fg="#FFFFFF", bg="#323232", padx=5, pady=5)
entry = Entry(root, textvariable=userInput, font="TkFixedFont", fg="#FFFFFF", bg="#1E1E1E")
submit_button = Button(root, text="Submit", command=submit, font="TkFixedFont", fg="#000000", bg="#FFFFFF")
spacing = Label(root, pady=2, fg="#55FF55", bg="#323232")
turtle_text = Label(root, text='"Welcome to the TURTLE TRAINER 3000!"', font="TkFixedFont", fg="#FFFFFF", bg="#323232")
turtle_art = Label(root, text="""               __  
    .,-;-;-,. /'_\ 
  _/_/_/_|_\_\) /  
'-<_><_><_><_>=/\  
  `/_/====/_/-'\_\ 
   ""     ""    "" """, font="TkFixedFont", fg="#55FF55", bg="#323232")

# Packing items (displays on screen)
to_pack = [label, entry, submit_button, spacing, turtle_text, turtle_art]
for item in to_pack:
    item.pack()

# Start functions
roll()

# Mainloops
# NOTE: DO NOT PUT ANY CODE AFTER THIS
root.mainloop()
