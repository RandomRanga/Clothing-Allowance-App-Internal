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

# Label for name combobox
name_label = Label(root, text = "Who spent their allowance:")
name_label.pack()


# Set up list and variable for combobox
name_list = ["Nikau", "Hana", "Tia"]
chosen_name = StringVar()
chosen_name.set(name_list[0])

# Combobox to select name
name_box = ttk.Combobox(textvariable=chosen_name, state="readonly")
name_box['values'] = name_list
name_box.pack()


# Label for the price entry
price_label = Label(root, text = "Price of clothing:")
price_label.pack()

# Variable to store the cost
price = DoubleVar()
price.set("")

# Entry for user to enter amoun
price_entry = Entry(root, textvariable = price)
price_entry.pack()


# Runs the main loop
root.mainloop()
