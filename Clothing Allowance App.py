from tkinter import *
from tkinter import ttk


###### CLASS CODE ######

# Class so it is not repetitive for the children
class Child:
	'''Collects all info about each child, 
	stores it and then displays it.'''

	# Collects and stores all child's info.
	def __init__(self, name, allowance, bonus_cost):
		self.name = name
		self.allowance = allowance
		self.bonus_cost = bonus_cost
		child_list.append(self)


  	# buy method subtracts money from balance and ensures it is positive.

	def buy(self, price):
		if price > 0  and price <= self.allowance:
			self.allowance -= price
			return True
		else:
			return False



##### FUNCTION CODE #####


# Function to get child names
def create_name_list():
	name_list = []
	for child in child_list:
		name_list.append(child.name)
	return name_list


# Function that will update the balance of the allowance
def update_balance():
	balance_string = ""

	# Append each child's allowance
	for child in child_list:
		balance_string += "{}: ${:.2f}\n".format(child.name, child.allowance)

	children_details.set(balance_string)



# Buy item function for when someone buys an item
def buy_item(child):
	if child.buy(price.get()):
		button_feedback.set("Success, {} bought an item for ${:.2f}.".format(child.name, price.get()))

	else:
		button_feedback.set("Not enough money left in {}'s allowance or not valid price.".format(child.name))


# Function to make it all work
def manage_feedback():
	try:
		for child in child_list:
			if chosen_child.get() == child.name:
				buy_item(child)


		# Update the GUI
		update_balance()
		price.set("")

	except ValueError:
		button_feedback.set("Please enter a valid number.")






# Set up lists
child_list = []


# Puts childs info in , and prints it.
child1 = Child("Nikau", 300, 50)
child2 = Child("Hana", 300, 50)
child3 = Child("Tia", 300, 50)
child_names = create_name_list()





###### GUI CODE ######

# Create the window with title
root=Tk()
root.title("Clothing Allowance App")




# Frame for top part of app
top_frame = ttk.LabelFrame(root)
top_frame.grid(row=0, column=0, padx=10, pady=10, sticky="NSEW")




# Creates and sets the welcome text variable
welcome_text = StringVar()
welcome_text.set("Welcome! You can track and edit all your children's allowances and if they are on track to reach the goal.")

# Creates and grid the welcome label
welcome_label = ttk.Label(top_frame, textvariable=welcome_text, wraplength=300)
welcome_label.grid(row=0, column=0, columnspan=2, padx = 10, pady = 10)



# Creates and sets the children details variable
children_details = StringVar()


# Create the details label and pack it into the GUI
details_label = ttk.Label(top_frame, textvariable=children_details)
details_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)









# Frame for the bottom part of app
bottom_frame = ttk.LabelFrame(root)
bottom_frame.grid(row=1, column=0, padx=10, pady=10, sticky="NSEW")



# Label for child combobox
name_label = ttk.Label(bottom_frame, text = "Who spent their allowance:")
name_label.grid(row=3, column=0, padx = 10, pady = 10)

# Sets a option list for combobox
chosen_child = StringVar()
chosen_child.set(child_names[0])

# Combobox to select child
child_box = ttk.Combobox(bottom_frame, textvariable=chosen_child, state="readonly")
child_box['values'] = child_names
child_box.grid(row=3, column=1, padx = 10, pady = 10)



# Label for the price entry
price_label = ttk.Label(bottom_frame, text = "Price of clothing:")
price_label.grid(row=4, column=0, padx = 10, pady = 10)

# Variable to store the cost
price = DoubleVar()
price.set("")

# Entry for user to enter amoun
price_entry = ttk.Entry(bottom_frame, textvariable = price)
price_entry.grid(row=4, column=1, padx = 10 , pady = 10)



# Sumbit button to sumbit it when you finished.
submit_button = ttk.Button(bottom_frame, text="Submit", command = manage_feedback)
submit_button.grid(row=6, column=0, columnspan=2, padx=10, pady=10)

# Feedback label so the user knows what happend
button_feedback = StringVar()
button_feedback_label = ttk.Label(bottom_frame, textvariable=button_feedback)
button_feedback_label.grid(row=7, column=0, columnspan=2)


# Runs the main loop
update_balance()
root.mainloop()