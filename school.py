class Student:
    def __init__(self, id, name, clss_no):
        self.id = id
        self.name = name
        self.clss_no = clss_no

    def printer(self):
        print(" {} {} {} ".format(self.id, self.name, self.clss_no))

    Student_1 = Student(18456,'Simple, Simon', 2)
    Student_2 = Student(18495, 'Dan, Matt', 3)
    Student_3 = Student(18489, 'Jack, Smithson', 2)
    Student_4 = Student(18499, 'John, Paul', 1)

    
