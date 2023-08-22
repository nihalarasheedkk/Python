# class Student:
#     rolno:int
#     name:str
#     course:str

#     def __init__(self,**kwargs):
#         self.rolno=kwargs.get("rolno")
#         self.name=kwargs.get("name")
#         self.course=kwargs.get("course")

#     def get_student(self):
#         print(self.rolno,self.name,self.course)

# obj=Student(rolno=1000,name="vijay",course="django")

# obj.get_student()

# class Books:
#     name:str
#     author:str
#     price:int
#     pages:int

#     def __init__(self,**kwargs):
#         self.name=kwargs.get("name")
#         self.author=kwargs.get("author")
#         self.price=kwargs.get("price")
#         self.pages=kwargs.get("pages")

#     def __str__(self):
#         return self.name  #__str__ is like given to get the um string representation exludin age,height

# obj=Books(name="randamoozham",author="mt",price=560,pages=500) 
# print(obj)  


#inheritance:
#overriding cheynel inherit cheythindaavanm
#  __str__ 


class Mobile(object):
    name:str
    price:int
    display:str

    def __init__(self,**kwargs): #constructor
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")

    def __str__(self):  #string method
        return self.name

obj=Mobile(name="oneplus",price=30000,display="amoled")
print(obj)        
        