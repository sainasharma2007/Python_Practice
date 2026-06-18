class Student:
    def __init__(self,marks):
        self.marks=marks

list=[]

s1= Student(65)
list.append(s1.marks)

s2=Student(34)
list.append(s2.marks)

s3=Student(87)
list.append(s3.marks)

s4=Student(98)
list.append(s4.marks)

s5=Student(55)
list.append(s5.marks)

s6=Student(90)
list.append(s6.marks)

list.sort()
print(list)