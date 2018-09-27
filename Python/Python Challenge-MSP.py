word = input("Player 1, what's the word? \n")

print ("\n" * 50)

aVariable = 0
def executioner():
    x = ("-----|", "     O ",  "     |", "     |\ ", "    /|\ ", "    /","    / \ ")

    for stuff in range(0,aVariable):
        if aVariable <= 3:
            print(x[stuff])
        if aVariable == 4:
            if stuff is not 2:
                print(x[stuff])
        if aVariable == 5:
            if stuff is not 2 and stuff is not 3:
                print(x[stuff])
        if aVariable == 6:
            if stuff is not 2 and stuff is not 3:
                print(x[stuff])
        if aVariable == 7:
            if stuff is not 2 and stuff is not 3 and stuff is not 5:
                print(x[stuff])

                
word1 = list(word)
myLen = len(word1)
loc = 0

blanks = []

for letters in word1:
    blanks.append("_")

print(" ".join(blanks), "\n" * 4)

while aVariable < 7:
    guess = input("Player 2, guess a letter: \n")

    for loc,letters in enumerate(word1):
        if guess == letters:
            blanks[loc]=guess
        
    if guess not in word1:
        aVariable = aVariable + 1
        executioner()
    print(" ".join(blanks))
    if "_" not in blanks:
        print("\nYou won!")
        break

print("\nGame Over")

