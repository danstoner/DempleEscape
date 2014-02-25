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
        enter_treasure_chamber()
    elif "2" in choice or "3" in choice:
        print "You step on a dark stone that depresses slightly."
    else:
        what()
        enter_long_hall()

def enter_treasure_chamber():
    print room_texts['treasure_chamber']
    choice = get_choice()
    if "4" in choice:
        enter_exit()
    elif "1" in choice or "2" in choice or "3" in choice:
        print "The instant you touch the treasure the room goes dark."
    else:
        what()

def enter_exit():
    print room_texts['exit']
    exit(0)

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
  
start()

# the fallout condition
print """
You fall down a hole and slide into an underground river.
After what seems like a very long time, you emerge into daylight and crawl ashore.

You will never find your way back to the temple and the possible treasure inside!
"""

exit(0)


# room_texts = {
#     "entrance":"""

# ****** Welcome to Demple Escape ******

# You are standing at the entrance to the hidden temple.

# Do you wish to:
# 1. enter the temple
# 2. run away like a baby 
# """,
#     "first_chamber":"""
# You are in the first chamber.  A large stone now blocks the entrance behind you.
# A small stone statue stand before you.

# Choose:
# 1. take statue
# 2. go deeper into the temple
# """,
#     "long_hall":"""
# You are in a very long hall lit by torches.
# You notice that some of the stones are slightly darker than the rest.

# As you walk down the hall, do you:
# 1. avoid the dark stones
# 2. step only on dark stones
# 3. walk carelessly without paying attention
# """,
#     "treasure_chamber":"""

# You have found the treasure chamber!

# All around you are piles of gold and precious gems.
# In the center of the room is a huge diamond.

# What do you do?
# 1. do not touch the huge diamond but take everything else you can carry
# 2. grab the huge diamond first
# 3. take only gold
# 4. exit through the doorway on the far side of the room without taking anything
# """,
#     "exit":"""
# Congratulations! You found the exit and survived the temple!
# Unfortunately you did not collect any treasure.

# Enjoy the rest of your life!
# """
# }
