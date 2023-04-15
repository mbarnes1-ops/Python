print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure, but beware, \
death lurks around every corner!")
cross_roads = input("You arrive at a cross road. \
Do you wish to go left or right?\n").lower()
if cross_roads == "left":
    lake = input("You come to a lake, which has an island in the middle. \
    Type 'wait' to wait for a boat, or 'swim' to swim across.\n").lower()
    if lake == "wait":
        door = input("You arrive at the island unharmed, \
        and find yourself in front of a house with three doors. \
        One door is red, one is yellow, and one is blue. \
        Which color do you choose?\n").lower()
        if door == "red":
            print("The door opens into the very pit of hell. \
                You are devoured by flames. Game Over.")
        elif door == "blue":
            print("The door opens and an angry wizard casts magic at you. \
                Your body is immediately frozen and shatters. Game Over.")
        elif door == "yellow":
            print("The door opens and you see a small box, \
sitting on the floor. Opening it, you find riches beyond \
your wildest dreams! You have won!")
        else:
            print("You die. Game over.")
    else:
        print("You attempt to swim the lake, as you are quite fit. \
        Midway to the island though you find that you never seem to get \
        closer and end up drowning. Game Over.")
else:
    print("You find yourself more and more lost, and starve to death. \
Game over.")
