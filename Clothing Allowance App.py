from tkinter import *
from tkinter import ttk


# Creates the window with title
root=Tk()
root.title("Clothing Allowance App")

# Create and set the welcome text variable
welcome_text = StringVar()
welcome_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the welcome label
welcome_label = Label(root, textvariable=welcome_text, wraplength=300)
welcome_label.pack()



# Runs the main loop
root.mainloop()
