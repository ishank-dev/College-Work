class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    
    def details(self):
        print("\nName: ",self.name,"\nAge: ",self.age,"\nMarks: ",self.marks)

    def accept(self):
        self.name=input('Enter name: ')
        self.age=int(input('Enter Age: '))
        for i in range(3):
            self.marks.append(int(input('Enter m'+str(i+1)+": ")))

Student('Rahul','20',[94,92,98]).details()
stud = Student('','',[])
stud.accept()
stud.details()
        