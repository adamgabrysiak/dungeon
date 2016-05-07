from tkinter import *

class Application(Frame):

	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.quit_button = Button(self, text = "Quit", command = self.quit_game)
		self.quit_button.grid(row = 0, column = 99, sticky = E)
		self.output_box = Text(self, width = 50, height = 10, wrap = WORD)
		message = " "
		self.output_box.grid(row= 1, columnspan = 100)
		self.display_message(message)
		self.inventory_button = Button(self, text = "Inventory", command = self.show_inventory) #not ready yet, for test purposes
		self.inventory_button.grid(row = 0, column = 1, sticky = W)
		self.statistics_button = Button(self, text = "Statistics", command = self.show_statistics) #not ready yet, for test purposes
		self.statistics_button.grid(row = 0, column = 2, sticky = W)
		self.button("Start")

	
	def display_message(self, text): #displays  text in the output_box
		self.output_box.delete(0.0, END)
		self.output_box.insert(0.0, text)

	def show_inventory(self): #creates window with inventory

		inventory_window = Toplevel()
		inventory_window.title("Inventory")
		message = Message(inventory_window, text = "The inventory will be displayed here")
		message.pack()

	def show_statistics(self): #creates window with stats

		statistics_window = Toplevel()
		statistics_window.title("Statistics")
		message = Message(statistics_window, text = "The statistics will be displayed here")
		message.pack()

	def button(self, action): #top left button with multiple purposes defined in the method

		try:
			self.primary_button.destroy()
		except:
			pass

		self.primary_button = Button(self, text = action)
		self.primary_button.grid(row = 0, sticky = W)

		if action == "Start":
			self.primary_button["command"] = self.main_area_game #callback to creation of the character should go here

		elif action == "Explore":
			self.primary_button["command"] = self.explore

		elif action == "Go back":
			self.primary_button["command"] = self.main_area_game

	def quit_game(self): #closing application
		exit()

	def main_area_game(self): #The main area message.
		message = "You are at your campside"
		self.display_message(message)
		self.button("Explore")

	def explore(self): #Explore message
		message = "You explore some shit"
		self.display_message(message)
		self.button("Go back")

if __name__ == "__main__":
	root = Tk()
	root.title("Graphical User Interface Test")
	app = Application(root)
	app.pack()
	root.mainloop()
