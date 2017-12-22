#RPG Game (THE HOUSE)
#By KingAneurnin
print("""
        Hello and Welcome To The House!
    
        Goal: Survive as Long As Your Can!
        
        Please Choose Your Character Type:
""")

#Imports random for future use.
import random

#Introduces the class types and starting variables so no errors occur.

hp = 0
atk = 0
df = 0
magic = 0
xp = 0
classTrue = False

print("""
==============================================================
Warrior: A powerful fighter.    HP: 150 ATK: 15 DF:  5 MAG:  0
--------------------------------------------------------------
Mage: A powerful debuffer.      HP: 100 ATK:  5 DF:  5 MAG: 30
--------------------------------------------------------------
Rogue: Weak, but hard to hit.   HP:  75 ATK:  7 DF: 10 MAG:  0
==============================================================""")

#Ask the user for the class they wish to have and only allow a valid answer.

player = input("\nWhat class do you wish to play as? ")

while classTrue != True:

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
    elif player.title() == "Rogue":
        hp = 75
        atk = 7
        df = 10
        classTrue = True
    else:
        player = input("\aPlease enter a Valid Class. ")

#Shows the player their choice.

print("\nYou have chosen the",player,"class, with\n",hp,"Health Points\n"
      ,atk,"Attack Points\n",df,"Defense Points\n",magic,"Magic.")
input("\nPress enter to continue.")

#Shows status of player.

def showStatus():
    print("\n=========================" + '''
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
        
#Prints commands possible

def controls():
    print("\nSay \"go [compass direction]\" to go a certain way where there is a door [] from your current location." +
          "\nCompass Directions = North, South, East, West.")
    print("\nSay \"get [item name]\" to get a certain item.")


#Sets the rooms and items for the game.

rooms = {
            1: { "name" : "Atrium",
                 "east" : 2,
                 "west" : 4,
                 "south": 6,
                 "north": 7, },
            2: { "name" : "Living Room",
                 "north": 3,
                 "west" : 1, },
            3: { "name" : "Bedroom",
                 "south": 2,
                 "item" : "sword"},
            4: { "name" : "Dining Room",
                 "north": 5,
                 "east" : 1,                  
                 "item" : "steak" },
            5: { "name" : "Kitchen",
                 "south": 4, },
            6: { "name" : "Yard",
                 "north": 1, 
                 "item" : "chicken"},
            7: { "name" : "Court Yard",
                 "south": 1, }
        }

#Random Monster Generator

monsters = { 1: {"name" : "Grizzly Bear",
                 "mhp"  : random.randint(35, 65),
                 "matk" : random.randint(5, 20),
                 "mdf"  : random.randint(5, 10),
                 "mxp"  : 10},
             2: {"name" : "Spider",
                 "mhp"  : random.randint(5, 25),                 
                 "matk" : random.randint(2, 10),
                 "mdf"  : random.randint(1, 3),
                 "mxp"  : 5}, 
             3: {"name" : "Tiger",
                 "mhp"  : random.randint(20, 30),                 
                 "matk" : random.randint(5, 15),
                 "mdf"  : random.randint(5, 10),
                 "mxp"  : 10}, 
             4: {"name" : "Sasquatch",
                 "mhp"  : random.randint(40, 70),                 
                 "matk" : random.randint(10, 15),
                 "mdf"  : random.randint(5, 10),
                 "mxp"  : 15}, 
             5: {"name" : "Coyote",
                 "mhp"  : random.randint(15, 35),                 
                 "matk" : random.randint(15, 20),
                 "mdf"  : random.randint(5, 10),
                 "mxp"  : 15}, 
             6: {"name" : "Wolf",
                 "mhp"  : random.randint(20, 25),
                 "matk" : random.randint(5, 10),
                 "mdf"  : random.randint(10, 15),
                 "mxp"  : 15}, 
             7: {"name" : "Ninja",
                 "mhp"  : random.randint(40, 80),                 
                 "matk" : random.randint(10, 15),
                 "mdf"  : random.randint(10, 20),
                 "mxp"  : 20}
           }

#Sets inventory for item usage.

inventory = [ "coins", ]


#Start Player in Atrium

currentRoom = 1

#Begins loop for playing until death.

while hp > 0:
    showStatus()
    controls()
    move = input("\n> ").lower().split()

    try:
        if move[0] == "go":
            if move[1] in rooms[currentRoom]:
                currentRoom = rooms[currentRoom][move[1]]
            else:
                input("You cannot go that way! Press enter to continue.")
    except:
        input("\a\nINVALID INPUT! PLEASE TRY AGAIN! PRESS ENTER TO CONTINUE.\n")
        continue

    try:
        if move[0] == "get":
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]["item"]:
                print("You received the " + move[1] + "!")
                inventory.append(rooms[currentRoom]["item"])

                #Item Attribute Addition
                
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
            else:
                input("No " + move[1] + " avalible to receive! Press enter to continue.")
    except:
        input("\a\nINVALID INPUT! PLEASE TRY AGAIN! PRESS ENTER TO CONTINUE.\n")
        continue

    #COMBAT SYSTEM/SIMULATOR:
    ###########################################################################
    
    x = random.randint(1,5)

    #Calls Monster Into Battle 20% of Time

    if x == 1:
       
        monsterNumber = random.randint(1, 7)
        monster = monsters[monsterNumber]
        monsterName = monsters[monsterNumber]["name"]
        
        print("\nYou are attacked by a " + monsterName + "!")
        
        mhp = monsters[monsterNumber]["mhp"]
        matk = monsters[monsterNumber]["matk"]
        mdf = monsters[monsterNumber]["mdf"]
        
        print("It has",mhp,"HP,",matk,"ATK, and",mdf,"DF!")

        #Pre-Combat Choices for Mages w/ Tests for Validity

        validChoice = False

        if player.title() == "Mage":

            while validChoice != True:

                decide = input("\nWould you like to cast a spell? \"Yes\" or \"No\"? ")

                if decide.title() == "Yes":
                    try: decide = int(input("\nEnter the number associated with the spell you desire:" +
                                   "\n\n1: INCREASE YOUR DEFENSE PERMANENTLY BY 10" +
                                   "\nCOST: 15 MAGIC" +
                                   "\n\n2: FIREBALL: KILL OPPONENT" +
                                   "\nCOST:  5 MAGIC"
                                   "\n\n> " ))
                    except: print("SPELL DID NOT WORK!")

                    if decide == 1 and magic >= 15:
                        df += 10
                        magic -= 15
                        print("\nYou now have",df,"Defense Points and",magic,"Magic.")
                        validChoice = True
                    elif decide == 2 and magic >= 5:
                        mhp = 0
                        magic -= 5
                        print("\nYou have slayed the " + monsterName + "!" +
                              "\nYou have",magic,"Magic remaining.")
                        input("\nPress enter to continue.")
                        validChoice = True
                        continue
                    elif magic >= 5:
                        print("VALID SPELL NOT CHOSEN! PLEASE TRY AGAIN!")
                    else:
                        print("Your spell failed! You only have",magic,"Magic !")
                        validChoice = True

                elif decide.title() == "No":
                    print("\nYou did not cast any spells!")
                    validChoice = True
        
        input("\nPress enter to commence the battle!\n")

        #Automates the Battle
        
        while mhp > 0 and hp > 0:
            shp = hp
            hp -= (matk - df)
            if hp > shp:
                print("You are immune to their attack!")
                hp = shp
                print("You have",hp,"HP left!\n")
            elif hp <= 0:
                print("You have fallen!" +
                      "\nGame Over!" )
                break
            else:
                print("You are wounded! Your HP is now " + str(hp) + "!")
            
            smhp = mhp
            mhp -= (atk - mdf)
            if mhp > smhp:
                print("It is immune to your attack!")
                mhp = smhp
                print("It has",mhp,"HP left!\n")
            elif mhp <= 0:
                print("It has fallen!\n")
                xp += monsters[monsterNumber]["mxp"]
                print("You now have",xp,"XP.")
                break
            else:
                print("You wounded it! Its HP is now " + str(mhp) + "!\n")

            ### For draws:

            if mhp == smhp and hp == shp:
                input("You both are at a draw! You both flee the battle." +
                      "\n\nPress enter to continue.")
                break

        
              
input("\n\nPress enter to exit the program.")
