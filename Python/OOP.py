

class Student:
    def __init__(self,name,Class,gender):
        self.name = name
        self.Class = Class
        self.gender = gender # type: ignore

    def __str__(self):  
        return f"Name = {self.name}, Class = {self.Class}, Gender= {self.gender} "
   


Students = []

name = input("Enter your name: ")
Class = input("Enter your class: ")
Gender = input("Enter your gender(M/F): ")
while Gender not in ( 'F','M'):
    print("Invalid Gender")
    Gende = input("Enter a valid gender(M/F): ")

Student_1 = Student(name,Class,Gender)
print(Student_1)