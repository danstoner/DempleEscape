# Demple Escape - (Dan's Temple Escape) - text-based adventure game
# by Dan Stoner
# 
# Major content contributions by:
# Avery Stoner and Julia Stoner
#
# License: GPL v2
# 
#
# Notes:
# Inspired by examples 35,36 in the Learn Python the Hard Way tutorial series
# http://learnpythonthehardway.org/


# Declarations
room_texts_filename = "room_texts.yaml"
#room_texts_filename = "test.yaml"   # for testing


from sys import exit

try:
    import yaml
except ImportError:
    print ("**Error: failed to import yaml module. Please install Python yaml module.**")

def what():
    print "I do not understand."

def get_choice():
    return raw_input("> ")

def dead(reason):
    print reason
    exit(0)

def start():
    print room_texts['entrance']
    choice = get_choice()
    if "1" in choice:
        enter_first_chamber()
    elif "2" in choice:
        dead("On your way home you are bitten by a snake and die. The End.")
    else:
        what()
        start()

def enter_first_chamber():
    print room_texts['first_chamber']
    choice = get_choice()
    if "2" in choice:
        enter_long_hall()
    elif "1" in choice:
        print """
As you touch the statue you feel the floor shake.
"""
    else:
        what()
        enter_first_chamber()

def enter_long_hall():
    print room_texts['long_hall']
    choice = get_choice()
    if "1" in choice:
        enter_cursed_room()
    elif "2" in choice or "3" in choice:
        print "You step on a dark stone and feel it depress slightly."
    else:
        what()
        enter_long_hall()

def enter_cursed_room():
    print room_texts['cursed_room']
    choice = get_choice()
    if "1" in choice:
        enter_magic_room()
    elif "2" in choice:
        dead("You feel a strange buzzing sensation and then find yourself unable to breath. \nIt appears that you are on the surface of the moon!")
    elif "3" in choice:
        enter_cursed_room()
    elif "4" in choice:
        enter_chasm()
    elif "5" in choice():
        enter_exit()
    else:
        what()
        enter_cursed_room()

def enter_chasm():
    print room_texts['chasm']
    choice = get_choice()
    if "1" in choice:
        dead("Aaaaahhhh....  You fall to your doom!")
    elif "2" in choice:
        enter_treasure_chamber()
    elif "3" in choice:
        dead("Aaaaahhhh....  You fall to your doom!")
    else:
        what()
        enter_chasm()

def enter_magic_room():
    print room_texts['magic_room']
    choice = get_choice()
    if "1" in choice:
        enter_cursed_room()
    elif "2" in choice:
        print "\nYou see a bucket at the end of the rope.\n"
        enter_magic_room()
    elif "3" in choice:
        dead("The rope pulls back! You fall into the bottom of the well and are never heard from again!")
    else:
        what()
        enter_magic_room()


def enter_treasure_chamber():
    print room_texts['treasure_chamber']
    choice = get_choice()
    if "4" in choice:
        enter_exit()
    elif "2" in choice:
        print "The diamond is large and beautiful!"
        enter_diamond_exit()
    elif "1" in choice or "3" in choice:
        print "The instant you touch the treasure the room goes dark."
    else:
        what()
        enter_treasure_chamber()

def enter_diamond_exit():
    print room_texts['diamond_exit']
    exit (0)

def enter_exit():
    print room_texts['exit']
    exit(0)

def fallout():
    print """

You fall down a hole and slide into an underground river.
After what seems like a very long time, you emerge into daylight and crawl ashore.

You will never find your way back to the temple and the possible treasure inside!

"""

#######  BEGIN main Program #####

# see if room_texts exists and read it into a dictionary
try:
    room_texts_yaml = yaml.safe_load(file(room_texts_filename, 'r'))
except yaml.YAMLError, exc:
    print "**Error in room data file**", exc

# convert the yaml version to more simple lookup dictionary
# room_texts = {'headroom':'This is the first element in the dictionary'}
room_texts = {}
for room in room_texts_yaml:
    room_name = room['room']
    room_description = room['description']
    room_texts[room_name] = room_description

# Enter the Temple!!!  
start()

# the fallout condition
fallout()

exit(0)


