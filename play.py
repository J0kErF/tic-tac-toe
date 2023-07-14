import os
import random
import platform

#the original mat
mat = [
        0,1,2,
        3,4,5,
        6,7,8
    ]

# receive the user choice
def getOpponent():
    index = int(input("enter cell number:"))
    if mat[index]=='O' or mat[index]=='X':
        print("Illegal Cell!")
        return getOpponent()
    else:
        return index


# checks if the game has ended by win or draw
def gameEnd():
    if mat[0]==mat[1]==mat[2]:
        print ("the winner is "+mat[0])
        return True
    elif mat[3]==mat[4]==mat[5]:
        print ("the winner is "+mat[3])
        return True
    elif mat[6]==mat[7]==mat[8]:
        print ("the winner is "+mat[6])
        return True
    elif mat[0]==mat[3]==mat[6]:
        print ("the winner is "+mat[0])
        return True
    elif mat[1]==mat[4]==mat[7]:
        print ("the winner is "+mat[1])
        return True
    elif mat[2]==mat[5]==mat[8]:
        print ("the winner is "+mat[2])
        return True
    elif mat[0]==mat[4]==mat[8]:
        print ("the winner is "+mat[0])
        return True
    elif mat[2]==mat[4]==mat[6]:
        print ("the winner is "+mat[2])
        return True
    for pos in mat:
        if isinstance(pos,(int,float)):
            return False
    print("Draw :\ ")
    return True
###################################################
# draw each point on it's own
def drawIt(x):
    for i in range(1, 10):
        if i == x[1]:
            if x[0] == 1:
                mat[i]='X'
            else:
                mat[i]='O'
# print a list of points
def draw(*args):
    for point in args:
        drawIt(point)
    print(mat)
###################################################

#--------------TO-DO---------------------------
#   here I should implement the algorithm of playing the tic-tac-toe 

# TO-DO: implement minimax algorithm
def getMoveHard():
    return

# let the pc play it randomly
def getMoveEasy():
    mop=(op+1)%2
    index = random.randint(0, 9)
    while mat[index]=='O' or mat[index]=='X':
        index = random.randint(0, 9)
    return index
###################################################
#here we print the game with the updated values
def display():
    if platform.system()=='windows':
        os.system('cls')
    else:
        os.system('clear')
    print(str(mat[0])+" | "+str(mat[1])+" | "+str(mat[2])+"\n---------\n"+str(mat[3])+" | "+str(mat[4])+" | "+str(mat[5])+"\n---------\n"+str(mat[6])+" | "+str(mat[7])+" | "+str(mat[8])+"\n")
    return 0
###################################################

xo = input("Choose your side [x,o]: ")
op=0
if xo == 'x' or xo == 'X':
    op=1
val=0

display()
if op==1:
    mat[getOpponent()]='X'
while True:
    val= getMoveEasy()
    if op ==1:  
        mat[val]='O'
    else:
        mat[val]='X'
    display()
    if gameEnd()==True:
        break
    val= getOpponent()
    if op ==1:  
        mat[val]='X'
    else:
        mat[val]='O'
    display()
    if gameEnd()==True:
        break