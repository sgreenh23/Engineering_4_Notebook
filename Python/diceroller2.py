import random
min = 1
max = 6

roll_again = "enter"

while roll_again == "enter" or roll_again == "enter":
    print "Rolling the dices..."
    print "The values are...."
    print random.randint(min, max)
    print random.randint(min, max)

    roll_again = raw_input("Roll the dices again?")
    
