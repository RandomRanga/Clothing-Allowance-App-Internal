from tkinter import *
from tkinter import ttk


###### CLASS CODE ######

# Class to hold children's info so isn't repetitive. 
class Child:
	'''
	Collects all info about each child, stores it, and then displays it.
	'''

	# Collects and stores all child's info.
	def __init__(self, name, allowance, bonus_cost):
		self.name = name
		self.allowance = allowance
		self.bonus_cost = bonus_cost
		child_list.append(self)


  	# Checks if anything is wrong with price and raises an exception error else takes price away from allowance. 
	def buy(self, price):
		if price <= 0:
			raise Exception ("Negative value")
		if price > self.allowance:
			raise Exception ("Value exceeds allowance")
		self.allowance -= price
		return True

	# Calculates if the bonus is possible for each child, then returns either string to display. 
	def get_progress(self):
		if self.allowance >= 50:
			progress =  "On target for bonus."
		else:
			progress =  "Bonus not possible."
		return progress





##### FUNCTION CODE #####


# Creates a list and puts the children's names in it. 
def create_name_list():
	name_list = []
	for child in child_list:
		name_list.append(child.name)
	return name_list


# Updates the allowance display of each child, and calls get_progress to show if they can get the bonus. 
def update_balance():
	balance_string = ""
	for child in child_list:
		progress= child.get_progress()
		balance_string += "{}: ${:.2f}  - {}\n".format(child.name, child.allowance, progress)

	children_details.set(balance_string)




# Used when someone buys an item to update the button_feedback text.
def buy_item(child):
	try:
		if child.buy(price.get()):
			button_feedback.set("Success, {} bought an item for ${:.2f}.".format(child.name, price.get()))
			
	except Exception as e:
		error = e.args[0]
		if error == "Negative value":
			button_feedback.set("Please enter a positive number.")
		elif error == "Value exceeds allowance":
			button_feedback.set("Sorry {} does not have sufficient allowance left.".format(child.name))
		else:
			button_feedback.set("Please enter a valid number.")




# Checks if the chosen name is in child_list then lets that child buy_item, updates GUI, and clears price entry. 
def manage_feedback():
	for child in child_list:
		if chosen_child.get() == child.name:
			buy_item(child)

	update_balance()
	price.set("")







# Sets up lists.
child_list = []


# Enters children's info.
child1 = Child("Nikau", 300, 50)
child2 = Child("Hana", 300, 50)
child3 = Child("Tia", 300, 50)

# defines list of names
child_names = create_name_list()






###### GUI CODE ######

# Creates a window with a title.
root=Tk()
root.title("Clothing Allowance App")




# Frame for the top part of the app.
top_frame = ttk.LabelFrame(root)
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")



# Creates and sets the welcome text variable.
welcome_text = StringVar()
welcome_text.set("Welcome! You can track and edit all your children's allowances and if they are on track to reach the goal.")

# Creates and places the welcome label.
welcome_label = ttk.Label(top_frame, textvariable=welcome_text, wraplength=300)
welcome_label.grid(row=0, column=0, columnspan=2, padx = 10, pady = 10)



# Declares the children details variable.
children_details = StringVar()


# Create the details label and places it in the GUI.
details_label = ttk.Label(top_frame, textvariable=children_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)







# Frame for the bottom part of the app.
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")


# Label for the child combobox and places it.
name_label = ttk.Label(bottom_frame, text = "Who spent their allowance:")
name_label.grid(row=3, column=0, padx = 10, pady = 10)

# Creates variable and option list for child_box combobox.
chosen_child = StringVar()
chosen_child.set(child_names[0])

# Combobox to select which child and places it.
child_box = ttk.Combobox(bottom_frame, textvariable=chosen_child, state="readonly")
child_box['values'] = child_names
child_box.grid(row=3, column=1, padx = 10, pady = 10)



# Label for the price entry.
price_label = ttk.Label(bottom_frame, text = "Price of clothing:")
price_label.grid(row=4, column=0, padx = 10, pady = 10)

# Variable to store the price of the item.
price = DoubleVar()
price.set("")

# Entry for the user to enter the price of an item.
price_entry = ttk.Entry(bottom_frame, textvariable = price)
price_entry.grid(row=4, column=1, padx = 10 , pady = 10)



# Submit button to submit price when the user has finished.
submit_button = ttk.Button(bottom_frame, text="Submit", command = manage_feedback)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Feedback label so the user knows what happened.
button_feedback = StringVar()
button_feedback_label = ttk.Label(bottom_frame, textvariable=button_feedback)
button_feedback_label.grid(row=7, column=0, columnspan=2)


# Runs the main loop and code.
update_balance()
root.mainloop()