class Student:
    def __init__(self,name,student_id,courses):
        self.name=name
        self.student_id=student_id
        self.courses=courses
    
    def add_course(self,course):
        self.courses.append(course)

    def display_infor(self):
        print("Name:",self.name)
        print("Student ID:",self.student_id)
        print("Courses:",self.courses)

student1=Student("Le Ngoc Bao Tran","22521506",[])
student1.add_course ("Python Programing")
student1.add_course ("Web Development")
student1.display_infor()

        