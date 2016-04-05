import random

def ranloc():
  location = []
  intro = random.randrange(2)
  mid = random.randrange(4)
  end = random.randrange(2)

  introdesc = {0 : "a grand hall",
               1 : "a room",}
  middesc = {0 : "which is lit by a single torch. The light gives the promise of safety alas false.",
             1 : "that resembles a torture chamber. \nVarious tools which sole purpose of existence is to inflict pain.\nThey are lying on the wooden bench which looks like it was heavily stained by large amounts of blood.",
             2 : "which you think served as prison. On eastern and western walls there are cells. \nThe iron bars look like you could contract tenatus just by looking at them",
             3 : "that looks like an abandoned canteen. There are traceses of a long fought battle in here. \nLong tables and benches, partly rotten from the humididty that engulfs whole location, overwhelm the room taking all the space."}
  exitdesc = {0 : "north",
            1 : "south"}
  print("\nYou are in a", introdesc[intro], middesc[mid], "\nYou can exit this location by going", exitdesc[end])

