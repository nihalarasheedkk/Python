class Mobile(object):  #is A
    name:str
    price:int
    display:str

    def __init__(self,**kwargs):
        self.name=kwargs.get("name")
        self.price=kwargs.get("price")
        self.display=kwargs.get("display")

    def __str__(self):
        return self.name
    # **
    @property
    def get_disc_price(self):
        return self.price-1000
    #decorators:to see a method as an attribute(brackets wont be there)

#**
obj=Mobile(name="oneplus",price=30000,display="amoled")    #constructor,string method,get method
# print(obj)  #__str__ 
print(obj.get_disc_price)     