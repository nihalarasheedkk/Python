# num1=int(input("enter a number "))

# num2=int(input("enter a number"))

# try:
#     res=num1/num2
#     print("result",res)   #doubtfull error-try block

# except Exception as e:
#     print("exception occured")      #to handle-except block

# print("db.commit1")
# print("db.commit2")

lst=[10,20,30,40,50]

location=int(input("enter the location of the list to fetch"))

try:
    print(lst[location])
except Exception as e:
    print(e.args)
print("dbcommit")
print("file read")    