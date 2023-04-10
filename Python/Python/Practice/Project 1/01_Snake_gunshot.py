import random
# Snake Water Gun or Rock Paper Scissors
def gameWin(comp, you):
    #If two value is equal, declare a tie!
    if comp == you:
        return None
    
    #Check for all posibilities when computer choose s
    elif comp == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
     #Check for all posibilities when computer choose w

    elif comp == 'w':
        if you == 'g':
            return False
        elif you == 's':
            return True
    #Check for all posibilities when computer choose g

    elif comp == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True
print("Comp turn : Water(W) Snake(S) or Gun(G)?")
randNo = random.randint(1,3)
if randNo == 1:
    comp ='s'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

you = input("Your Turn:Water(W) Snake(S) or Gun(G)?")
a = gameWin (comp, you)

print(f"Computer chose {comp}")
print(f"You Choose {you}")

if a== None:
    print("The game id tie!")
elif a:
    print("You Win!")
else:
    print("You Lose!")