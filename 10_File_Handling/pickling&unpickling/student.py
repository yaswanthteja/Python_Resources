class Student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    
    def display(self):
        print(f'nameis {self.name} \n,roll no is {self.rollno}\n,marks is {self.marks}')

