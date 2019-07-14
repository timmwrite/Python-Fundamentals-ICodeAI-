class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def printer(self):
        print("Hello my name is {} and am {} and my gender is {}".format(self.name, self.age, self.gender))

    Student_1 = Student('JOhn', 20, 'male')
    Student_2 = Student('Mark', 23, 'male')
    Student_3 = Student('Val', 30, 'male')

class Teacher(Student):
    def who_am_i(self):
        print('I am a Teacher')
    def set_college(self):
        self.college = input('Enter the college: ')
        return self.college

Teacher_1 = Teacher('Allan', 27, 'Male')

