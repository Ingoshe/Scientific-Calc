from tkinter import *
from math import *

# Function to perform calculations
def calculate():
    try:
        result = eval(entry.get())
        label.config(text = str(result))
    except:
        label.config(text = "Invalid input")

# Create the main window
root = Tk()
root.title("Scientific Calculator")

# Create a label to display the result
label = Label(root, text = "", width = 30)
label.grid(row = 0, column = 0, columnspan = 4)

# Create buttons for digits and operations
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    Button(root, text = button, width = 5, command = lambda button=button: click(button)).grid(row = row_val, column = col_val)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Function to handle button clicks
def click(button):
    current = entry.get()
    if button == '=':
        try:
            result = eval(current)
            label.config(text = str(result))
            entry.delete(0, END)
        except:
            label.config(text = "Invalid input")
            entry.delete(0, END)
    elif button == 'C':
        entry.delete(0, END)
        label.config(text = "")
    else:
        entry.insert(END, button)

# Create an entry field for user input
entry = Entry(root, width = 30)
entry.grid(row = 0, column = 0, columnspan = 4)

# Create a button for clear
Button(root, text = 'C', width = 5, command = lambda: click('C')).grid(row = 1, column = 4)

# Start the main loop
root.mainloop()
