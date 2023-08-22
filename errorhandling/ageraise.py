# age=int(input("enter a age"))

# if age<18:
#     raise Exception("invalid age")

# else:
#     print("valid")



#add

num=input("enter a number")

if type(num)==int:
    print(num**3)
else:
    raise Exception("operand must be integer")