# Automatic Dice Roller
# Written by SHoaplhliiae

from random import randint



print("Automatic Dice Roller")
print("Press 'enter' to roll, 'x' to exit")
answer = input()

while answer.lower() == "":
    num = randint(1,6)
    print ("You rolled a", num)
    print ("Roll again?")
    answer = input()

#while answer.lower() == "x":
print ("program over")
