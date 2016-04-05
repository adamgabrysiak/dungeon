import random

def ranloc():
  location = []
  intro = random.randrange(2)
  mid = random.randrange(2)
  end = random.randrange(2)

  introdesc = {0 : "a large cave",
               1 : "a room"}
  middesc = {0 : "which is lit by a single torch.",
             1 : "that resembles a torture chamber."}
  exitdesc = {0 : "north",
            1 : "south"}
  print("You are in a", introdesc[intro], middesc[mid], "You can exit this location by going", exitdesc[end])

  input("Press enter...")
