# pacman
Implementation of Pacman without using pygame or any additional game-making library. The game asks user to enter an integer n, which will be the size of the grid. Player has 2n units of energy. The player has to move from origin point on grid (random) to the goal, avoiding obstancles and collecting points. The moves allowed are U,D,L,R standing for up down, left and right. Player can make multiple moves in one go (in the form: U2R5L8). Each of these moves costs 1 unit of energy. If player runs into an onstancle, 4n units of energy are lost. The game ends when the player runs out of energy. Two special move costing n/2 units of energy are allowed- A and C i.e. clockwise and anticlockwise rotation.

The following classes are defined:

1.
Name: grid 
About: Instance is the grid in which the game is played
Attributes: n: Represents no. of rows and coolumns in the playing grid. Taken as input from user. [Integer]
            start: Contains the point on the grid where player starts from. This is taken at random. [Tuple]
            goal: Contains the point on the grid where the player is supposed to reach. This is taken at random. [Tuple]
            myObstancles: Randomly generated list of objects of the type obstancle which will be randomly spawned throughout the grid.                               [List]
            myRewards: Randomly generated list of objects of the type reward which will be randomly spawned throughout the grid. [List]
Methods: gridr: Sets up grid
         showgrid: prints the grid
         rotateAntiClockwise and rotateClockwise: for rotation (a special move)
         
2.
Name: obstancle
About: Instance of this class represents an obstancle on the game grid. Represented by #.
Atrributes: x: x coordinate of the obstancle on the grid. [Integer]
            y: y coordinate of the obstancle on the grid. [Integer]

3.
Name: reward
About: Instance of this class represents a reward on the game grid. Represented by the value of energy it holds.
Atrributes:x: x coordinate of the obstancle on the grid. [Integer]
              y: y coordinate of the obstancle on the grid. [Integer]
              value: the value of energy held by the particular reward. This is randomly decided. [Integer in range 0-9]

4.
Name: player
About: Instance of this class is the player that is moved on the grid to collect rewards and avoid obstancles.
Atrributes: x: x coordinate of Player. [Integer]
            y: y  coordinate of Player. [Integer]
            Energy: The energy left with player. [Integer]
Methods: makemove: Changes coordinates of player as per command entered by user.
         
