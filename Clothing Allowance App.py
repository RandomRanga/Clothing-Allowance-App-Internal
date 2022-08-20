from tkinter import *
from tkinter import ttk


# Create the window with title
root=Tk()
root.title("Clothing Allowance App")

# Create and set the welcome text variable
welcome_text = StringVar()
welcome_text.set("Welcome! You can deposit or withdraw money and see your progress towards your goals.")

# Create and pack the welcome label
welcome_label = Label(root, textvariable=welcome_text, wraplength=300)
welcome_label.pack()

# Label for the price entry
price_label = Label(root, text="Price of clothing:")
price_label.pack()

# Variable to store the cost
price = DoubleVar()
price.set("")

# Entry for user to enter amount
price_entry = Entry(root, textvariable = price)
price_entry.pack()






# Runs the main loop
root.mainloop()
