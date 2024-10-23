class Person:
    name=''
    age=''
    def __init__(self,_name,_age):
        self.name=_name
        self.age=_age

    def Introduce(self):
        return f'Tôi tên là {self.name},{self.age} tuổi'
    
class Student(Person):
    def __init__(self,_name,_age,_ID,_GPA):
        super().__init__(_name,_age)
        self.ID=_ID
        self.GPA=_GPA

    def Introduce(self):
        CLASSSUPER=super().Introduce()
        return self.ID,self.GPA
        

    def Get_grade(self):
        if self.GPA >= 3.6:
            HS=f'{self.name} là học sinh xuất sắc'
        elif self.GPA >=3.2 and self.GPA<3.6:
            HS=f'{self.name} là học sinh giỏi'
        elif self.GPA >= 2.5 and self.GPA<3.2:
            HS=f'{self.name} là học sinh khá'
        elif self.GPA <=2.5:
            HS=f'{self.name} là học sinh trung bình'
        return HS


name=input("Học sinh đó tên là: ")
age=int(input("Học sinh đó có số tuổi là: "))
ID=int(input("Mã ID của học sinh đó là: "))
GPA=float(input("Số GPA(điểm trung bình) của học sinh đó là: "))

student=Student(name,age,ID,GPA)
print(student.Get_grade())