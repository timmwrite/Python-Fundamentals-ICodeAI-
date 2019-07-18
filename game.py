#The game of Life, devised by the British mathematician John H. Conway

class Organism:
    def __init__(self, col, row):

        self.col = col
        self.row = row

#Creat a 2d array 
    def new_array(self, my_array):
        self.new_array = [[0 for a in range(self.col)] for b in range(self.row)]
        return self.new_array

#Create a new generation
    def new_generation(self):
        return self.new_generation

#Insert new organism
    def new_organism(self):
        return self.new_organism

#Get the position of the elements 
    def get_position_of_elements(self):
        pass

#Set the rules of the game 
    def game_rules():
        pass