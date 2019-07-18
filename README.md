#The game of Life, devised by the British mathematician John H. Conway

#The procedures
#Create a new store -> 2D-Array
#Creating a new Organism
#Inserting the newly created Organism
#Access the postion of each element
#Iterate through the store(Checking for the neiboughood)
#Set the rules of the game
#    -If a cell is alive and has either two or three live neighbors, the cell remains alive in the next generation.
#    -A living cell that has no live neighbours or a single live neighbour dies from isolation in the next generation.
#    -A living cell that has four or more live neighbours dies from overpopulation in the next generation.
#    -A dead cell with exactly three live neighbours results in birth and becomes alive in the next generation. All other dead cells remain dead in the next Generation.

The game starts with an initial configuration supplied by the user. Successive
generations are created by applying the set of rules simultaneously to each cell in
the grid. Interesting patterns can develop as the population of organisms undergoes
changes by expanding or eventually dying out. To illustrate the game of Life,
consider the following simple configuration of live organisms:

Applying the rules to this configuration creates the next generation. This results
in two organisms dying (shown below as the light grey boxes) based on rule 2, one
remaining alive based on rule 1, and the generation of a new organism based on
rule 4 (the black box marked with an x).

If we evolve the next generation, the system dies out since both live cells in the
first-generation has a single live neighbour

While some systems may eventually die out, others can evolve into a “stable"
state. Consider the following initial configuration and its first generation. The result is a stable
state since the four live cells each have three neighbours and no
dead cell has exactly three neighbours in order to produce a new live cell.

Another interesting pattern is the “two-phase oscillator," which alternates
between successive generations:
