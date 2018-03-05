class Student(object):
    def __init__(self, name):
        self.name = name
    def study(self):
        print self.name,"studying..."

stud = Student("Mark Watson")
stud.study()

