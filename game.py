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




class Organism:
    def __init__(self, col, row):

        self.col = col
        self.row = row

#Create a new store -> 2D-Array 
    def new_array(self, my_array):
        self.new_array = [[0 for a in range(self.col)] for b in range(self.row)]
        return self.new_array

#Creating a new Organism
    def new_Organism(self):
        return self.new_Organism

#Inserting the newly created Organisms
    def new_organism(self):
        return self.new_organism

#Access the postion of each element 
    def get_position_of_elements(self):
        pass
    
#Iterate through the store(Checking for the neiboughood)
    def neibouhood_organisms(self):
        pass
    
#Set the rules of the game 
    def game_rules():
        pass
