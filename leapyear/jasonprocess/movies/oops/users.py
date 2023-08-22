class Users:
    data=[
        {"id":1,"username":"jhon","email":"jhon@gmail.com","password":"password@123"},
        {"id":2,"username":"hari","email":"hari@gmail.com","password":"password@123"},
        {"id":3,"username":"ravi","email":"ravi@gmail.com","password":"password@123"},
        {"id":4,"username":"vijay","email":"vijay@gmail.com","password":"password@123"},
        {"id":5,"username":"vinu","email":"vinu@gmail.com","password":"password@123"},
        {"id":6,"username":"tom","email":"tom@gmail.com","password":"password@123"},   #attribute=> data
    ]

    #get all usr name
def get_all_users(self):
        return self.data
    
def getuser_detail(self,id):
        return [u for u in self.data if u.get("id")==id]
    
    #to update with a new user
def post(self,obj):
        self.data.append(obj)
        return obj
    

# print(obj.getuser_detail(2))

#TO DESTROY

# def destroy(self,id):  #id=6
#     obj=[u for u in self.data if u.get("id")==id][0]
#     self.data.remove(obj)
    

obj=Users()
# obj.destroy(5)
# print(obj.get())




   
def put(self,id,value):
     obj=[u for u in self.data i]        



obj=Users()
data={"id":5,"username":"vinus","email":"vinus@gmail.com","password":"password@123"}

obj.put(5,data)
# user_data={"id":7,"username":"ram","email":"ram@gmail.com","password":"password@123"}
# obj.post(user_data)
# print(obj.get_all_users())     #add ayikko nokan




