# RPG Game (THE HOUSE)
# By KingAneurnin

# Imports random for future use.
import random


def log(the_file, text, show=True):
    """Program used to log the combat data."""
    with open(the_file, "a+") as f:
        f.write(text)
        f.write("\n")
        f.close()
    if show:
        print(text)


print("""
        Hello and Welcome To The House!
    
        Goal: Survive as Long As Your Can!
        
        Please Choose Your Character Type:
""")

# Introduces the class types and starting variables so no errors occur.

hp = 0  # health points
atk = 0  # attack points
df = 0  # defense points
magic = 0  # magic points (Mages Only)
xp = 0  # experience points
lxp = 5  # experience points to level up (increases over time)
lvl = 1  # starting level

print("""
==============================================================
Warrior: A powerful fighter.    HP: 150 ATK: 15 DF:  5 MAG:  0
--------------------------------------------------------------
Mage: A powerful buffer.        HP: 100 ATK:  5 DF:  5 MAG: 30
--------------------------------------------------------------
Rouge: Weak, but hard to hit.   HP:  75 ATK:  7 DF: 10 MAG:  0
==============================================================""")

# Ask the user for the class they wish to have and only allow a valid answer.

player = input("\nWhat class do you wish to play as? ")

classTrue = False
while not classTrue:

    if player.title() == "Warrior":
        hp = 150
        atk = 15
        df = 5
        classTrue = True
    elif player.title() == "Mage":
        hp = 100
        atk = 5
        df = 5
        magic = 30
        classTrue = True
    elif player.title() == "Rouge":
        hp = 75
        atk = 7
        df = 10
        classTrue = True
    elif player.title() == "God":  # For Game Testing
        hp = 1
        atk = 100
        df = 100
        classTrue = True
    else:
        player = input("\aPlease enter a Valid Class. ")

# Shows the player their choice.

print("\nYou have chosen the", player, "class, with\n", hp, "Health Points\n"
      , atk, "Attack Points\n", df, "Defense Points\n", magic, "Magic.")

# Asks for player name

name = input("What is your character name?\n> ")

# Logs name without printing for logging game sessions.

log("battle.txt", ("\n\n" + name + " HP: " + str(hp) + " ATK: " + str(atk) + " DF: " + str(df) + " MAG: " + str(magic) +
                   "\n=============================="), False)

input("\nPress enter to continue.")


# Shows status of player.

def show_status():
    print("\n" + "Name: " + name + " HP: " + str(hp) + " ATK: " + str(atk) + " DF: " + str(df) + " MAG: " + str(magic))
    print("===========================================" + '''
+-----------+---------------+-------------+
|           |               |             |
|           |               |             |
|  Kitchen  |  Court Yard   |   Bedroom   |
|           |               |             |
|           |               |             |
|           |               |             |
+----[ ]-----------[ ]------------[ ]-----+
|           |               |             |
|   Dining [ ]    Atrium   [ ]   Living   |       N
|   Room    |               |    Room     |       ^
|           |               |             |       |
+-----------+------[ ]------+-------------+ W <-------> E
|                                         |       |
|                   Yard                  |       v
|                                         |       S
+-----------------------------------------+
''' +
          "\n=========================")
    print("You are in the " + rooms[currentRoom]["name"])
    print("=========================")
    if "item" in rooms[currentRoom]:
        print("=========================")
        print("You see a " + rooms[currentRoom]["item"] + "!")
        print("=========================")


# Prints commands possible

def controls():
    print("\nSay \"go [compass direction]\" to go a certain way where there is a door [] from your current location." +
          "\nCompass Directions = North, South, East, West.")
    print("\nSay \"get [item name]\" to get a certain item.")
    print("\nSay \"end game\" to end the game.")


# Sets the rooms and items for the game.

rooms = {
    1: {"name": "Atrium",
        "east": 2,
        "west": 4,
        "south": 6,
        "north": 7, },
    2: {"name": "Living Room",
        "north": 3,
        "west": 1, },
    3: {"name": "Bedroom",
        "south": 2,
        "item": "sword"},
    4: {"name": "Dining Room",
        "north": 5,
        "east": 1,
        "item": "steak"},
    5: {"name": "Kitchen",
        "south": 4, },
    6: {"name": "Yard",
        "north": 1,
        "item": "chicken"},
    7: {"name": "Court Yard",
        "south": 1, }
}

# Random Monster Generator

monsters = {1: {"name": "Grizzly Bear",
                "mhp": random.randint(35, 65),
                "matk": random.randint(5, 20),
                "mdf": random.randint(5, 10),
                "mxp": 10},
            2: {"name": "Spider",
                "mhp": random.randint(5, 25),
                "matk": random.randint(2, 10),
                "mdf": random.randint(1, 3),
                "mxp": 5},
            3: {"name": "Tiger",
                "mhp": random.randint(20, 30),
                "matk": random.randint(5, 15),
                "mdf": random.randint(5, 10),
                "mxp": 10},
            4: {"name": "Werewolf",
                "mhp": random.randint(40, 70),
                "matk": random.randint(10, 15),
                "mdf": random.randint(5, 10),
                "mxp": 15},
            5: {"name": "Coyote",
                "mhp": random.randint(15, 35),
                "matk": random.randint(15, 20),
                "mdf": random.randint(5, 10),
                "mxp": 15},
            6: {"name": "Wolf",
                "mhp": random.randint(20, 25),
                "matk": random.randint(5, 10),
                "mdf": random.randint(10, 15),
                "mxp": 15},
            7: {"name": "Assassin",
                "mhp": random.randint(40, 80),
                "matk": random.randint(10, 15),
                "mdf": random.randint(10, 20),
                "mxp": 20}
            }

# Sets inventory for item usage.

inventory = ["coins", ]

# Start Player in Atrium

currentRoom = 1

# Begins loop for playing until death.

while hp > 0:
    show_status()
    controls()
    move = input("\n> ").lower().split()

    try:
        if move[0] == "go":
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                input("You cannot go that way! Press enter to continue.")
    except IndexError:
        input("\a\nINVALID INPUT! PLEASE TRY AGAIN! PRESS ENTER TO CONTINUE.\n")
        continue

    try:
        if move[0] == "get":
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
                print("You received the " + move[1] + "!")
                inventory.append(rooms[currentRoom]["item"])

                # Item Attribute Addition

                if "steak" in inventory and "steak" in rooms[currentRoom]["item"]:
                    hp += 25
                    print("Your HP increased by 25! It is now " + str(hp) + "!")

                if "chicken" in inventory and "chicken" in rooms[currentRoom]["item"] and player.title() == "Mage":
                    magic += 15
                    print("Your MAG increased by 15! It is now " + str(magic) + "!")

                elif "chicken" in inventory and "chicken" in rooms[currentRoom]["item"]:
                    df += 5
                    print("Your DF increased by 5! It is now " + str(df) + "!")

                if "sword" in inventory and "sword" in rooms[currentRoom]["item"]:
                    atk += 5
                    print("Your ATK increased by 5! It is now " + str(atk) + "!")

                del rooms[currentRoom]["item"]
                input("\nPress enter to continue.")
                continue
            else:
                input("No " + move[1] + " available to receive! Press enter to continue.")
    except IndexError:
        input("\a\nINVALID INPUT! PLEASE TRY AGAIN! PRESS ENTER TO CONTINUE.\n")
        continue

    try:
        if move[0] == "end":
            if "game" == move[1]:
                log("battle.txt", "\nXXXXXXXXXX Game Ended XXXXXXXXXX")
                break
    except IndexError:
        input("\a\nINVALID INPUT! PLEASE TRY AGAIN! PRESS ENTER TO CONTINUE.\n")
        continue

    # COMBAT SYSTEM/SIMULATOR:
    ###########################################################################

    x = random.randint(1, 4)

    # Calls Monster Into Battle 25% of Time & Logs for Battle Log

    if x == 1:

        monsterNumber = random.randint(1, 7)
        monsterName = monsters[monsterNumber]["name"]

        log("battle.txt", "\nYou are attacked by a " + monsterName + "!")

        mhp = monsters[monsterNumber]["mhp"]
        matk = monsters[monsterNumber]["matk"]
        mdf = monsters[monsterNumber]["mdf"]

        log("battle.txt", "It has " + str(mhp) + " HP, " + str(matk) + " ATK, and " + str(mdf) + " DF!\n")

        log("battle.txt", "You currently have " + str(hp) + " HP, " + str(atk) + " ATK, "
            + str(df) + " DF, and " + str(magic) + " MAG!\n")

        # Pre-Combat Choices for Mages w/ Tests for Validity

        validChoice = False

        if player.title() == "Mage":

            while not validChoice:

                decide = input("\nWould you like to cast a spell? \"Yes\" or \"No\"? ")

                if decide.title() == "Yes":
                    try:
                        decide = int(input("\nEnter the number associated with the spell you desire:" +
                                           "\n\n1: INCREASE YOUR DEFENSE PERMANENTLY BY 10" +
                                           "\nCOST: 15 MAGIC" +
                                           "\n\n2: FIREBALL: KILL OPPONENT" +
                                           "\nCOST:  5 MAGIC"
                                           "\n\n> "))
                    except TypeError:
                        print("SPELL DID NOT WORK!")

                    if decide == 1 and magic >= 15:
                        df += 10
                        magic -= 15
                        log("battle.txt",
                            ("\nYou now have " + str(df) + " Defense Points and " + str(magic) + " Magic."))
                        input("\nPress enter to commence the battle!\n")
                        validChoice = True
                    elif decide == 2 and magic >= 5:
                        mhp = 0
                        magic -= 5
                        log("battle.txt", "\nYou have slayed the " + monsterName + " with a Fireball!" +
                            "\nYou have " + str(magic) + " Magic remaining.")
                        input("\nPress enter to continue.")
                        validChoice = True
                        continue
                    elif magic >= 5:
                        print("VALID SPELL NOT CHOSEN! PLEASE TRY AGAIN!")
                    else:
                        print("Your spell failed! You only have", magic, "Magic!")
                        input("\nPress enter to commence the battle!\n")
                        validChoice = True

                elif decide.title() == "No":
                    print("\nYou did not cast any spells!")
                    input("\nPress enter to commence the battle!\n")
                    validChoice = True

        else:
            input("\nPress enter to commence the battle!\n")

        # Automates the Battle & Records

        while mhp > 0 and hp > 0:
            shp = hp
            hp -= (matk - df)
            if hp > shp or (matk - df) == 0:
                log("battle.txt", "You are immune to their attack!")
                hp = shp
                log("battle.txt", ("You have " + str(hp) + " HP left!"))
            elif hp <= 0:
                log("battle.txt", "You have fallen!" +
                    "\nGame Over!\n")
                break
            else:
                log("battle.txt", ("You are wounded! Your HP is now " + str(hp) + "!" + " (-" + str(matk - df) + ")"))

            smhp = mhp
            mhp -= (atk - mdf)
            if mhp > smhp or (atk - mdf) == 0:
                log("battle.txt", "It is immune to your attack!")
                mhp = smhp
                log("battle.txt", ("It has " + str(mhp) + " HP left!"))
            elif mhp <= 0:
                log("battle.txt", "It has fallen!\n")
                xp += monsters[monsterNumber]["mxp"]
                print("You now have", xp, "XP." + "(+" + str(monsters[monsterNumber]["mxp"]) + ")")
                break
            else:
                log("battle.txt", ("You wounded it! Its HP is now " + str(mhp) + "!" + " (-" + str(atk - mdf) + ")"))

            # For draws:

            if mhp == smhp and hp == shp:
                log("battle.txt", "You both are at a draw! You both flee the battle.\n")
                input("\nPress enter to continue.")
                break

    # Level Up System
    while xp >= lxp and hp > 0:
        lvl += 1
        print("You are now level " + str(lvl) + "!")
        lxp *= 2
        if xp < lxp:
            print("You need", (lxp - xp), "more XP to level up again.")
        input("\nPress enter to continue.\n")

input("\nPress enter to exit the program.")
