from tkinter import *

class Application(Frame):

    """Graphical user interface"""

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()

    def create(self):
        self.lbl1 = Label(self)
        self.lbl1["text"] = "Welcome to Pydungeon"
        self.lbl1["font"] = "Helvetica 16"
        self.lbl1.grid(row = 0, pady = 10)
        self.bttn2 = Button(self)
        self.bttn2["text"] = "Start"
        self.bttn2["command"] = self.start
        self.bttn2.grid(row = 1, column = 29, padx = 10, sticky = E)
        self.exbttn = Button(self)
        self.exbttn["text"] = "Quit"
        self.exbttn["command"] = self.exit
        self.exbttn.grid(row = 2, column = 29, pady = 10, padx = 10, sticky = E)

    def exit(self):
        exit()

    def start(self):
        app.lbl1.destroy()
        app.bttn2.destroy()
        self.namentr = Entry(self)
        self.namentr.grid(row = 0, column = 0, pady = 1, padx = 1, sticky = W)
        self.accbttn = Button(self, text = "enter", command = hero.getname)
        self.accbttn.grid(row = 1, column = 0, pady = 1, padx = 1, sticky = W)
        self.output = Text(self, width = 50, height = 10, wrap = WORD)
        message = "State your name and press enter"
        self.output.grid(columnspan = 30)
        self.show(message)

    #Method that displays text
    def show(self, text):
        app.output.delete(0.0, END)
        app.output.insert(0.0, text)

    def showtalentsgui(self):
        app.namentr.destroy()
        app.accbttn.destroy()
        self.bttnS = Button(self)
        self.bttnS["text"] = "Strenght"
        self.bttnS["command"] = hero.addstrg
        self.bttnS.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = W)
        self.bttnA = Button(self)
        self.bttnA["text"] = "Agility"
        self.bttnA["command"] = hero.addagi
        self.bttnA.grid(row = 0, column = 1, padx = 1, pady = 1, sticky = W)
        self.bttnV = Button(self)
        self.bttnV["text"] = "Vitality"
        self.bttnV["command"] = hero.addvit
        self.bttnV.grid(row = 0, column = 2, padx = 1, pady = 1, sticky = W)
        self.stats = Button(self)
        self.stats["text"] = "Statistics"
        self.stats["command"] = hero.stats
        self.stats.grid(row = 1, padx = 1, pady = 1, sticky = W)
        message = "Choose which atrribute is the most important for you. "
        self.show(message)

    def standard(self):
        self.explore = Button(self)
        self.explore["text"] = "Explore"
        self.explore["command"] = home.explore
        self.explore.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = W)
        self.inventory = Button(self)
        self.inventory["text"] = "Inventory"
        self.inventory["command"] = hero.inventory
        self.inventory.grid(row = 1, column = 1, padx = 1, pady = 1, sticky = W)
        home.camp

    def rev(self):
        app.explore.destroy()
        self.back = Button(self)
        self.back["text"] = "Go back"
        self.back["command"] = home.camp
        self.back.grid(row = 0, column = 0, padx = 1, pady = 1, sticky = W)

class Creation(object):

    """Everything regarding playable character"""

    strg = 5
    vit = 5
    agi = 5

    def getname(self):
        self.name = app.namentr.get()
        app.show("Your name is " + self.name)
        app.showtalentsgui()

    def addstrg(self):
        app.bttnS.destroy()
        app.bttnA.destroy()
        app.bttnV.destroy()
        self.strg += 5
        app.standard()

    def addagi(self):
        app.bttnS.destroy()
        app.bttnA.destroy()
        app.bttnV.destroy()
        self.agi += 5
        app.standard()

    def addvit(self):
        app.bttnS.destroy()
        app.bttnA.destroy()
        app.bttnV.destroy()
        self.vit += 5
        app.standard()

    def stats(self):
        app.show("Your character's name is " + self.name +
                 ". You have: " + str(self.strg) + " points of strenght, "
                 + str(self.agi) + " points of agility "
                 + str(self.vit) + " points of vitality")

    def inventory(self):
        #this will show inventory, nothing here now.
        message = "You have some items. Deal with it"
        app.show(message)
        app.rev()
        
class Safeplace(object):

    def camp(self):
        app.back.destroy()
        app.explore.destroy()
        app.inventory.destroy()
        app.standard()
        message = "You are safe now. This is the place that is familiar to you and can be called home. You can see simple tent where you sleep and a campfire."
        app.show(message)

    def explore(self):
        message = "You explore nearby area. Good for you."
        app.show(message)
        app.rev()


menu = Tk()
menu.title("pydungeongui")

app = Application(menu)
hero = Creation()
home = Safeplace()
app.create()
app.pack()
menu.mainloop()
