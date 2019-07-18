#2d rows and columns where individual elemenst can be accessed

class Dimention():
  def __init__(self):
      self.row = 0
      self.column = 0
      self.my_array = self.my_array = [[0 for i in range(column)], for i in range(row)]

  #Create a 2d array (matrix) and pass in rows and columns
  def create(self,rows,columns):
      self.row = row
      self.column = column
      self.my_array = self.my_array = [[0 for i in range(column)], for i in range(row)]
      return self.my_array

      
  #Access the number of rows and return the number of rows 
  def get_num_rows(self):
      for k in range(row):
          return self.row
  
  #Access the number of columns and return the number of columns
  def get_num_columns(self, row, column):
      self.my_array = [[value for i in range(column)], for i in range(row)]
      return self.my_array      
   
  #Clear the array
  def clear_array(self,value):
      self.my_array = my_array.clear()
  
  
  def get_item(self,row,column):
          return self.my_array[column][row]
  
  def set_item(self,row,column,item_value):
      self.my_array[column][row] = item_value
      return self.my_array