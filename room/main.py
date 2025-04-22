from room import Room
from item import Item
from character import Character
from character import Enemy

kitchen = Room("kitchen")
dining_hall = Room("dining_hall")
ballroom = Room("ballroom")

kitchen.set_description("A dank and dirty place, buzzing with flies")
dining_hall.set_description("An extravagent, out of place dining hall where gold plates every square inch of the room.")
ballroom.set_description("A run down pile of rubble. Not much room to dance and not many people to dance either. A couple of rusted locked chests catch your eye in the corner of the room.")

kitchen.get_description()
kitchen.describe()

kitchen.link_room(dining_hall,"south")
dining_hall.link_room(kitchen,"north")
dining_hall.link_room(ballroom,"west")
ballroom.link_room(dining_hall,"east")

#dining_hall.get_details()

current_room = kitchen

harbold = Character("Harold","A small, horrid smelling goblin who is anxious")
harbold.set_conversation("hrhrrhhrhhrrhrhr. gold gold gold everywhere.(looks at you with crazed eyes)can't you see this is heaven!!!")
#harbold.describe()
#harbold.talk()
kitchen.set_character(harbold)

alucard = Enemy("Alucard","A fearsome human/vampire hybrid who is struggling to grasp his identity.")
alucard.set_weakness("stake")
alucard.set_conversation("Go away. I have no need for you to betray me. leave me alone and i will show you mercy.")
alucard.set_loss_message("(teleports behind you, grabs you and throws you though the wall to the kitchen) This is the last time i ever give a human my grace.")
dining_hall.set_character(alucard)

fingleflop = Enemy("Fingleflop", "a towering dragon that uses its ears to fly")
fingleflop.set_conversation("Care to join me in the danse macabre?")
fingleflop.set_weakness("music")
fingleflop.set_loss_message("its like silence to my ears")
ballroom.set_character(fingleflop)


stick = Item("stick")
stick.set_description("brown and sticky")
stick.describe()
stick.set_role("to be stick to objects")
stick.get_role()
stick.print_role()


#game loop
inhabitant = current_room.get_character()
if inhabitant is not None:
    print("\n")
    inhabitant.describe()
while True:
    print("\n")
    current_room.get_details()
    command = input("- ")
    #check whether a direction was typed
    if command in ["north", "south", "east","west"]:
        current_room = current_room.move(command)
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            print("\n")
            inhabitant.describe()
    elif command == "talk":
        print("\n")
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            print("\n")
            inhabitant.talk()
    elif command == "fight":
        print("\n")
        inhabitant = current_room.get_character()
        if inhabitant is not None:
            print("\n")
            conclusion = inhabitant.fight(input("Choose the item you are going to fight with: "))
            if conclusion == False:
                inhabitant.say_loss_message()
                print("You lost! game over!")

                break








