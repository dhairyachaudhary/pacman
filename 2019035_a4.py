from os import system
from time import sleep
import random

#Class definitions

class grid():

    """
    Instance is the grid in which the game is played

    INSTANCE ATTRIBUTES:
    n: Represents no. of rows and coolumns in the playing grid. Taken as input from user. [Integer]
    start: Contains the point on the grid where player starts from. This is taken at random. [Tuple]
    goal: Contains the point on the grid where the player is supposed to reach. This is taken at random. [Tuple]
    myObstancles: Randomly generated list of objects of the type obstancle which will be randomly spawned throughout the grid. [List]
    myRewards: Randomly generated list of objects of the type reward which will be randomly spawned throughout the grid. [List]
    """

    def __init__(self, n, start, goal, myObstancles, myRewards):
        """
        Attributes of a grid of n size.
        Pre: All arguments must belong to correct category as specified above.
        """
        self.n=n
        self.start=start
        self.goal=goal
        self.myObstancles=myObstancles
        self.myRewards=myRewards

    def gridr(self,player):
        """
        Sets up the game grid.
        """
        thematrix=[]
        row=0
        while row<self.n:
            rowlist=[]
            col=0
            while col<self.n:
                p=False
                for a in self.myObstancles:
                    if a.x==col and a.y==row:
                        p=True
                q=False
                for a in self.myRewards:
                    if a.x==col and a.y==row:
                        q=True
                if player.x==col and player.y==row:
                    rowlist.append("O")
                elif self.goal[0]==col and self.goal[1]==row:
                    rowlist.append("G")
                elif p==True:
                    rowlist.append("#")
                elif q==True:
                    for a in self.myRewards:
                        if a.x==col:
                            val=a.value
                            rowlist.append(val)
                            break
                else:
                    rowlist.append(".")
                col=col+1
            row=row+1
            thematrix.append(rowlist)
        return (thematrix)

    def showgrid(self,g,p1):
        """
        Prints the grid (2-D array) onto the console.
        """
        row=0
        while row<self.n:
            col=0
            while col<self.n:
                if col==p1.x and row==p1.y:
                    print("O",end="")
                elif col==self.goal[0] and row==self.goal[1]:
                    print("G",end="")
                elif g[row][col]=="O":
                    print(".",end="")
                elif g[row][col]=="G":
                    print(".",end="")
                else:
                    print(g[row][col],end="")
                col=col+1
            row=row+1
            print("")

    def rotateAnticlockwise(self,mat):
        """
        Special move to rotate game grid anticlockwise.
        """
        a=self.n
        while a!=0:
            for x in range(0, int(self.n/2)):
                for y in range(x, self.n-x-1):
                    t=mat[x][y]
                    mat[x][y]=mat[y][self.n-1-x]
                    mat[y][self.n-1-x]=mat[self.n-1-x][self.n-1-y]
                    mat[self.n-1-x][self.n-1-y]=mat[self.n-1-y][x]
                    mat[self.n-1-y][x]=t
            a=a-1
            return mat

    def rotateClockwise(self,mat):
        """
        Special move to rotate game grid clockwise.
        """
        a=self.n
        while a!=0:
            for x in range(0, int(self.n/2)):
                for y in range(x, self.n-x-1):
                    t=mat[x][y]
                    mat[x][y]=mat[self.n-1-y][x]
                    mat[self.n-1-y][x]=mat[self.n-1-x][self.n-1-y]
                    mat[self.n-1-x][self.n-1-y]=mat[y][self.n-1-x]
                    mat[y][self.n-1-x]=t
            a=a-1
            return mat

class obstancle():
    """
    Instance of this class represents an obstancle on the game grid. Represented by #.

    INSTANCE ATTRIBUTES:
    x: x coordinate of the obstancle on the grid. [Integer]
    y: y coordinate of the obstancle on the grid. [Integer]
    """
    def __init__(self,x,y):
        """
        Coordinates of Obstancle
        Pre: Must be integers.
        """
        self.x=x
        self.y=y

class reward():
    """
    Instance of this class represents a reward on the game grid. Represented by the value of energy it holds.

    INSTANCE ATTRIBUTES:
    x: x coordinate of the obstancle on the grid. [Integer]
    y: y coordinate of the obstancle on the grid. [Integer]
    value: the value of energy held by the particular reward. This is randomly decided. [Integer in range 0-9]
    """
    def __init__(self,x,y,value):
        """
        Coordinates of reward and value associated with it.
        Pre: Must be integers.
        """
        self.x=x
        self.y=y
        self.value=value

class player():
    """
    Instance of this class is the player that is moved on the grid to collect rewards and avoid obstancles.

    INSTANCE ATTRIBUTES:
    x: x coordinate of Player. [Integer]
    y: y  coordinate of Player. [Integer]
    Energy: The energy left with player. Each move costs 1 unit of energy. Game is initialized with 2*n units, where n is taken as input from user. [Integer]

    Game ends when energy is zero.
    """
    def __init__(self,x,y,energy):
        """
        Coordinates and energy level of player.
        Pre: Must be integers.
        """
        self.x=x
        self.y=y
        self.energy=energy

    def makemove(self,s):
        """
        Changes coordinates of player as per command entered by user.
        """
        global n
        if s=="R":
            if self.x==n-1:
                self.x=0
            else:
                self.x=self.x+1
        elif s=="L":
            if self.x==0:
                self.x=n-1
            else:
                self.x=self.x-1
        elif s=="D":
            if self.y==n-1:
                self.y=0
            else:
                self.y=self.y+1
        else:
            if self.y==0:
                self.y=n-1
            else:
                self.y=self.y-1

#Helper functions

def update(grid,mat):
    """
    Helper function to update the grid after the clockwise or anticlockwise rotation function is called.
    """
    grid.myObstancles=[]
    grid.myRewards=[]
    row=0
    while row<n:
        col=0
        while col<n:
            if mat[row][col]=="#":
                grid.myObstancles.append(obstancle(col,row))
            elif mat[row][col]!="." and mat[row][col]!="O" and mat[row][col]!="G":
                grid.myRewards.append(reward(col,row,mat[row][col]))
            col=col+1
        row=row+1

def clear():
    """
    Helper function to clear screen. Used before execution of every new command.
    """
    _ = system('cls')

#This is where the Game starts

print("Welcome to Gridworld!")
print("Press P to start the game.")

while True:
    """
    This loop terminates when the player reaches goal or runs out of energy.
    """
    start=input()
    if start.upper()=="P":
        #Game Begins
        #Initializing all the values of the grid, some are taken as input (n) while others are randomly generated.

        n=int(input("Enter dimension of Grid:\n"))

        start=(random.randint(0, n-1),random.randint(0, n-1))

        while True:
            end=(random.randint(0, n-1),random.randint(0, n-1))
            #To ensure that starting point of player and goal don't coincide
            if end[0]!=start[0] and end[1]!=start[1]:
                break

        i=0
        ob=[]
        while i<n-1:
            x=random.randint(0,n-1)
            y=random.randint(0,n-1)
            if (x!=start[0] or y!=start[1]) and (x!=end[0] or y!=end[1]):
                #To ensure no obstancle coincides with starting point or ending point
                ob.append(obstancle(x,y))
                i=i+1

        i=0
        rew=[]
        while i<n-1:
            x=random.randint(0,n-1)
            y=random.randint(0,n-1)
            p=False
            for a in ob:
                if a.x==x and a.y==y:
                    p=True
            if (x!=start[0] or y!=start[1]) and (x!=end[0] or y!=end[1] and p==False):
                #To ensure no reward coincides with an object, the starting point or the ending point
                rew.append(reward(x,y,random.randint(1,9)))
                i=i+1

        #Initializing the grid in which game will be played and the player with these values
        gamegrid=grid(n, start,end,ob,rew)
        p1=player(gamegrid.start[0],gamegrid.start[1],2*n)

        clear()

        #Initializing the Output
        a=gamegrid.gridr(p1)
        gamegrid.showgrid(a,p1)
        print("Energy remaining: ", 2*n)
        sleep(0.25)

        while True:
            """This is the main loop of the game. Terminates at the same time as the loop in which it is present."""
            #Prompts user for new move after completion of each move. This happens till user wins or energy runs out.
            move=input("Next move:\n")
            while move!="":
                """
                Runs till complete move input by user is executed.
                """
                #times represents the number of times the next loop will be executed
                times=int(move[1])
                while times!=0:
                    """
                    Used to execute each move as many times as specified by user.
                    Runs as many times as value after a particular command of input.
                    """
                    #Executed for the classic moves
                    if move[0].upper()=="R" or move[0].upper()=="L" or move[0].upper()=="U" or move[0].upper()=="D":
                        p1.makemove(move[0].upper())
                        clear()
                        a=gamegrid.gridr(p1)
                        gamegrid.showgrid(a,p1)
                        p1.energy=p1.energy-1
                        print("Energy remaining: ", p1.energy)
                        if p1.energy==0:
                            print("Out of Energy! You lose.")
                            quit()
                        sleep(0.25)
                        times=times-1
                    #Executed for special moves
                    else:
                        clear()
                        if move[0].upper()=="C":
                            a=gamegrid.rotateClockwise(gamegrid.gridr(p1))
                            gamegrid.showgrid(a,p1)
                        elif move[0].upper()=="A":
                            a=gamegrid.rotateAnticlockwise(gamegrid.gridr(p1))
                            gamegrid.showgrid(a,p1)
                        update(gamegrid,a)
                        p1.energy=p1.energy//3
                        print("Energy remaining: ", p1.energy)
                        if p1.energy==0:
                            print("Out of Energy! You lose.")
                            quit()
                        sleep(0.25)
                        times=times-1

                    for a in gamegrid.myObstancles:
                        """
                        Checks if p1 has encountered an obstancle after every move made.
                        If so energy is reduced by n*4
                        Runs for as many times as there are obstancles present on the board.
                        """
                        if a.x==p1.x and a.y==p1.y:
                            p1.energy=p1.energy-n*4
                            gamegrid.myObstancles.remove(a)
                        if p1.energy<=0:
                            print("Encountered Obstancle: out of Energy! You lose.")
                            quit()

                    for a in gamegrid.myRewards:
                        """
                        Checks if p1 has landed on a reward at the end of a full move.
                        If so energy is increased by value of reward.
                        Runs for as many times as there are rewards present on the board.
                        """
                        if a.x==p1.x and a.y==p1.y:
                            p1.energy=p1.energy+a.value+1
                            gamegrid.myRewards.remove(a)
                move=move[2:]

            #Checks to see if player has landed on Goal after the execution of full move. If so game is won.
            if p1.x==gamegrid.goal[0] and p1.y==gamegrid.goal[1]:
                print("You win!")
                quit()
