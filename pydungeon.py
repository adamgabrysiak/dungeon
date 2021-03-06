import random
import os
import math
import location

#global
inv = [] #ekwipunek
command = None
answer = None
newitem = None
roomorder = [] #kolejność wyświetlania pokoi
price = 20 #cena itemow w sklepie

#enemies
enstr = 0 #siła wroga
enagi = 0 #zręczność wroga
envit = 0 #żywotność wroga
enhp = 0 #punkty życia wrogatat
enatt = 0 #siła ataku wroga
ename = None #nazwa wroga
fenatt = 0 #finalny atak wroga
enxp = 0 #xp za przeciwnika
engold = 0 #gold za zabicie stwora

#player
name = None #imię postaci
str = 5 #siła
agi = 5 #zręczność
vit = 5 #żywotność
hp = None #punkty życia
att = 0 #siła ataku
fatt = 0 #finalny atak postaci
pxp = 0 #xp bohatera
exp = 1 #xp potrzebne do nastepnego lvlu
plvl = 1 #lvl bohatera
gold = 0 #gold bohatera

#generowanie kolejności pokoi
i = 1
while i <= 10:
    j = random.randrange(10)
    if j not in roomorder:
        roomorder.append(j)
        i += 1


def menu():
    global command, answer, inv, name
    os.system("cls")
    print("\n\n\t\t**THE MAIN MENU**"
          "\n\n1. Create a new character and start a new game. (Start)"
          "\n2. Continue"
          "\n3. Exit")
    command = input(": ")
    command = command.lower()
    answer = ["start", "s", "continue", "c", "exit", "e"]
    invalid(answer)
    os.system("cls")
    if command == "start" or command == "s":
        champ()
    if command == "exit" or command == "e":
        exit()
    if command == "continue" or command == "c":
        if name == None:
            print("\nThere is nothing you can continue.")
            menu()
        else:
            start()

def showeq():
    global command, answer
    command = str(input("\nWould you like to see yout inventory? (yes/no): "))
    answer = ["yes", "no"]
    invalid(answer)
    os.system("cls")
    if command == "yes":
        eq()
    if command == "no":
        menu()

def eq():
    command = None
    global inv, vit, str, agi
    if "sword" in inv:
        str += 5
    elif "boots" in inv:
        agi += 5
    elif "armor" in inv:
        vit += 5
    elif "amulet" in inv:
        str += 5
        agi += 5
        vit += 5
    elif "steelplatearmor" in inv:
        vit += 10
    elif "axe" in inv:
        str += 10
    elif "rapidboots" in inv:
        agi += 10
    calcstats()
    print("\nYou have ", len(inv), "items in your inventory.\nYour inventory consists of: ")
    if len(inv) != 0:
        for item in inv:
            print(item)
    else:
        print("Nothing.")
    input()
    start()

def additem():
    global inv, answer, command, newitem
    if newitem == None:
        command = input("\nWould you like to add an item? (yes/no): ")
        answer = ["yes", "y", "no", "n"]
        invalid(answer)
        if command == "yes" or command == "y":
            newitem = input("\nWhat item do you want to add?: ")
            inv.append(newitem)
            print("Item has been added")
            newitem = None
            start()
        if command == "no" or command == "n":
            start()
    else:
        command = input("\nWould you like to add the item to your inventory?  (yes/no): ")
        answer = ["yes", "y", "no", "n"]
        invalid(answer)
        if command == "yes" or command == "y":
            if newitem in inv:
                print("You can't take two items of the same kind")
                command = input(": ")
            else:
                inv.append(newitem)
                print("Item has been added")
                newitem = None
                eq()
                start()
        if command == "no" or command == "n":
            start()

def invalid(answer):
    global command
    while command not in answer:
        print("Invalid answer. You can only use", answer, ". Try again.")
        command = input(": ")

def champ():
    global command, name, str, agi, vit, hp
    os.system("cls")
    clear()
    command = None
    name = input("\nState the name of the character: ")
    print("\nWhat is the strongest side of your character?: "
          "\n\t1. Strength"
          "\n\t2. Agility"
          "\n\t3. Vitality")
    command = input("\n:")
    answer = ["1","2","3"]
    invalid(answer)
    if command == "1":
        str += 2
    elif command == "2":
        agi += 2
    elif command == "3":
        vit += 2
    calcstats()
    start()

def start():
    global command, answer, inv
    os.system("cls")
    calcstats()
    print("\nFor some unknown to you reason you are imprisoned in a dark dungeon. \nYou are safe for now and you attend to your wounds."
          "\n\nIf you want to see", name, "'s inventory then write 'inventory'"
          "\nIf you want to go back to the menu write 'menu'"
          "\nIf you want to see", name, "'s statistics then write 'stats'"
          "\nIf you want to explore write 'explore'"
          "\nIf you want to visit a shop, write 'shop' or 'p'")
    command = input("\n: ")
    command = command.lower()
    answer = ["explore", "e", "inventory", "i", "menu", "m", "stats", "s", "debug", "shop", "p"]
    invalid(answer)
    if command == "inventory" or command == "i":
        eq()
    elif command == "explore" or command == "e":
        fight()
    elif command == "menu" or command == "m":
        menu()
    elif command == "stats" or command == "s":
        stats()
    elif command == "debug":
        additem()
    elif command == "shop" or command == "p":
        shop()

def fight():
    global hp, enhp, enatt, command, answer, name, att, fenatt, fatt, pxp, ename, gold, engold, plvl
    os.system("cls")
    if plvl > 2:
        location.defloc(roomorder)
    else:
        location.ranloc()
    randomenemy()
    if ename != None:
        while enhp > 0 and hp > 0:
            ranchance()
            print("\n", ename, " attacks! He hits", name, "for", fenatt, "points.")
            hp = hp - fenatt
            if hp <= 0:
                print("\nYou have lost. You are a disgrace to the mankind")
                input()
                clear()
                menu()
            print("\n", name, "has", hp, "health points and", ename, "has", enhp, "health points.")
            command = input("\nWould you like to fight or run like a little bitch?" "\nIf you have a healing potion you can heal your wounds.: " )
            answer = ["run", "r", "fight", "f", "heal", "h"]
            os.system("cls")
            invalid(answer)
            if command == "run" or command == "r":
                start()
            elif command == "fight" or command == "f":
                print("\nWith all your might you hit", ename, "for", fatt, "points.\nHe is confused as to why did you do that.")
                enhp = enhp - fatt
            elif command == "heal" or command == "h":
                if "healing potion" in inv:
                    calcstats()
                else:
                    print("You don't have a healing potion.")
        if enhp <= 0:
            print("\nYou have killed", ename, "and won. Yay. Your hero gains", enxp, "xp! And", engold, "gold!")
            dropitem()
            print("\n")
            pxp = enxp + pxp
            gold = gold + engold
            lvlup()
            if newitem != None:
                additem()
            else:
                input()
                start()
    else:
        print("You haven't found anything in the room.")
        input()
        start()

def stats():
    global name, vit, agi, str, hp, pxp, plvl
    os.system("cls")
    print("\n\nYour character's name is", name, ". \nHe has:\n", str, "points of strenght,\n", agi, "points of agility \n", vit, "points of vitality (which gives the character", hp, "health points.)", "\n Your character has:", pxp, "xp points.\n Your character has:", gold, "gold.\nYour character level is:", plvl, "\nYou need:", math.floor(10 * math.pow(exp,2)) - pxp, "xp points to lvl up")
    input()
    start()

def calcenstats():
    global envit, enhp, enatt, enstr, enagi
    enhp = envit * 10
    enatt = enstr * 2 + enagi * 2

def calcstats():
    global hp, vit, str, agi, att
    hp = vit * 10
    att = str * 2 + agi * 2

def clear():
    global name, str, vit, agi, hp, att, inv, newitem, pxp
    name = None
    str = 15
    vit = 15
    agi = 15
    pxp = 0
    att = None
    hp = None
    inv = []
    newitem = None

def randomenemy():
    global ename
    choice = random.randrange(100)
    if choice == 0:
        ename = None
    elif 0 < choice <= 10:
        ghoul()
    elif 10 < choice <= 20:
        troll()
    elif 20 < choice <= 30:
        janusz()
    elif 30 < choice <= 40:
        bardlord()
    elif 40 < choice <= 50:
        hobgoblin()
    elif 60 < choice <= 90:
        ghoul()
    elif 90 < choice <= 100:
        ename = None


def lvlup():
    global pxp, str, agi, vit, exp, plvl
    if pxp >= math.floor(10 * math.pow(exp,2)):
        plvl = plvl + 1
        addstats()
        calcstats()
        pxp = 0
        exp = exp * math.pow(1.1,2)
        print("Congratulations. You have achieved a new level   ")

def addstats():
    global str, agi, vit
    str = str + 1
    agi = agi + 1
    vit = vit + 1

def goblin():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "Goblin"
    enstr = 2
    enagi = 2
    envit = 2
    enxp = 2
    engold = 2
    calcenstats()
    print("\nYou have met a goblin. He is quite weak")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def hobgoblin():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "HobGoblin"
    enstr = 3
    enagi = 3
    envit = 3
    enxp = 3
    engold = 3
    calcenstats()
    print("\nYou have met a hobgoblin.\nA curious creature, undoubtly cousin of the goblin.\nJudging by the armor he donned he is the more accomplished one in the family of goblins.")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def ghoul():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "Ghoul"
    enstr = 4
    enagi = 4
    envit = 4
    enxp = 3
    engold = 4
    calcenstats()
    print("\nYou have met a ghoul. You've read about him. He really, really likes dead flesh.\nConsidering that you are still alive you are wondering what does he want from you.")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def troll():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "Troll"
    enstr = 5
    enagi = 1
    envit = 10
    enxp = 5
    engold = 5
    calcenstats()
    print("\nBefore you stands a mighty troll. He is as strong as he is ugly. \nHe grins at you and says 'Fresh meat'.")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def bardlord():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "Bardlord"
    enstr = 8
    enagi = 5
    envit = 5
    enxp = 8
    engold = 8
    calcenstats()
    print("\nWalking through the forest You encountered an ancient creature. It's a Bardlord from Summoner's Rift. He's collecting meeps peacefully, when suddenly ")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def janusz():
    global enstr, envit, enagi, enhp, ename, enxp, engold
    ename = "Janusz"
    enstr = 1
    enagi = 30
    envit = 5
    enxp = 10
    engold = 10
    calcenstats()
    print("\nIn the depths of this forsaken dungeon you meet a strange creature. He is scarily tall and his eyes gleam with unbound insanity.\nYou can hear him muttering angrily, over and over the same phrase.\n'WHY ARE THOSE CABLES AREN'T WORKING'")
    print("He has", enhp, "health points.")
    input()
    os.system("cls")

def dropitem():
    global newitem, ename
    choice = random.randrange(10)
    if choice == 0:
        newitem = "sword"
    elif choice == 1:
        newitem = "armor"
    elif choice == 2:
        newitem = "boots"
    elif choice == 3:
        newitem = "amulet"
    elif choice == 4:
        newitem = "healing potion"
    else:
        newitem = None
    if newitem != None:
        print("After looking at", ename, "'s dead body you see that he had", newitem)
    else:
        print("Bad luck. The enemy had nothing")

def ranchance():
    global enatt, att, fenatt, fatt
    ran = random.randrange(100)
    if 0 < ran < 10:
        attack = 0.0
    elif 10 <= ran < 30:
        attack = 0.5
    elif  30 <= ran < 50:
        attack = 0.75
    elif 50 <= ran < 70:
        attack = 1.0
    elif 70 <= ran < 90:
        attack = 1.25
    else:
        attack = 1.5
    fatt = att * attack
    fenatt = enatt * attack

def shop():
    global gold, price, newitem, inv, answer, command
    os.system("cls")
    print("You're entering a long forgotten store.\nThe owner of the shop greets you vigorously: \n'Hello wanderer! Come, come!\nWhat can I do for You?'"
    "\n\nYou can buy an Axe ( +10 strength ) for", price, "gold.\nTo buy an axe type a."
    "\n\nYou can buy a steel plate armor ( +10 vitality ) for", price, "gold.\nTo buy steel plate armor type s."
    "\n\nYou can buy a new pair of rapid boots ( +10 agility ) for", price, "gold.\nTo buy rapid boots type b."
    "\n\nYou can also sell your items. To do so type 'sell'."
    "\n\nIf you wish to exit the shop type 'exit'"
    "\n\nYou have", gold, "gold")
    command = input("\n: ")
    command = command.lower()
    answer = ["a", "s", "b", "exit", "e", "sell"]
    invalid(answer)
    os.system("cls")
    if command == "sell":
        if not inv:
            print("You don't have any items for sale.")
            input(": ")
            shop()
        else:
            sellitem()
    elif command == "exit" or command =="e":
        start()
    elif gold >= 20:
        if command == "a":
            newitem = "axe"
        elif command == "s":
            newitem = "steel plate armor"
        elif command == "b":
            newitem = "rapid boots"
        elif newitem in inv:
            print("You can't buy two items of the same kind!")
            command = input(": ")
            shop()
        inv.append(newitem)
        print("Item has been added")
        gold -= 20
        newitem = None
    elif gold < 20:
        print("You don't have enough gold You prick! Get out of here!")
        input()
        start()


def sellitem():
    global gold, inv, command, answer
    print("You have", len(inv), "items that You can sell:\n\n")
    for item in inv:
        print(item)
    command = input("\n\nWhat item would you like to sell?: ")
    answer = inv
    invalid(answer)
    inv.remove(command)
    gold += 10
    print(command, "has been sold")
    input()
    command = None
    start()

os.system("cls")
print("\n\n\t\tWelcome to the simple text game by Adam Gabrysiak and Mateusz Zagorski.")
input()
os.system("cls")
menu()
