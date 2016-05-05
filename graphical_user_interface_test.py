from tkinter import *

class Application(Frame):
	"""displaying"""

	def __init__(self, master):
		super(Application, self).__init__(master)
		self.pack()
		self.actions = Action()

	def button(self, action):
		self.primary_button = Button(self, text = action, command = self.actions.action_selection(action))
		return self.primary_button

class Action(object):
	"""logic and mechanics"""

	def __init__(self):
		#creating exit button
		Application.button(self, "exit")

	def action_selection(self, action):
		if action == "exit":
			return exit()

root = Tk()
root.title("Graphical User Interface Test")

app = Application(root)

root.mainloop()
