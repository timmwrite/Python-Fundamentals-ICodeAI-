#Add Items
#Pop an Element
#UPdate  an Element
#Union 



class Sets:
    def __init__(self):

        self.my_list = my_list()



    def add_elements(self, elements):

        """Add elements in the list.

        Args:
                Elements: The iterable items in the list.

        """
        self.set_2 = set_2.append(elements)
        self.set_1 = set_1.append(elements)

    def pop_item(self, element):

        """Remove a specific elements from the list.

        Args:
            Elements: The iterable items in the list.

        """
        self.set_2.pop(element)
        return self.set_2
   
    def update(self, elements):

        """Update the list elements.

        Args:
            Elements: The iterable items in the list.

        """
        self.set_2.update(elements)
        return self.set_2

    def union(self, set_1, set_2):

        """Union combines the elments in set_1 and set_2.

        Args:
            Elements: The iterable items in the list.

        """
        self.new_set = set_1.union(set_2)
        return self.new_set

    def intersection(self, set_1, set_2):



        self.new_intersection = set_1.intersection(set_2)
        return self.new_intersection

    def compare_sets(self, set_1, set_2):
        return [x for x, k in (zip(set_1, set_2)) if x == k]
        
    