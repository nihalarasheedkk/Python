class Employee:

    id:int
    name:str
    desig:str
    salarry:int

    def __init__(self,id,nyame,designtn,sal):
        self.id=id
        self.name=nyame
        self.desigg=designtn
        self.salarry=sal

    def get_emp(self):
        print(self.id,self.name,self.desigg,self.salarry)

emp1=Employee(1000,"rocky","hr",34000)


emp1.get_emp()