import student
import pickle

f=open('data.pkl','wb')
n=int(input("Enter a number of employees: "))
for i in range(n):
    name=input('Enter a name: ')
    rollno=int(input('Enter the roll no: '))
    marks=float(input('Enter  your marks: '))
    obj=student.Student(name,rollno,marks)
    pickle.dump(obj,f)  # pickling
    
print('Object stored success')
    


