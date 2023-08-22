class Student:
    rollno:int
    name:str
    course:str  #not needed

    def add_std_detail(self,rol,name,course):
        self.rollno=rol
        self.name=name
        self.course=course

    def get_student(self) :
        
