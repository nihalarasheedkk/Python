emp={"id":100,"name":"hari","desig":"HR","salary":250000}
# print(emp)
# print(emp["name"])

#iteration
# for key in emp:
    # print(key,emp[key])

#  emp["gender"]="male"  
# print(emp)  

# emp["name"]="nihala"
# print(emp)

# emp["salary"]+=1
# print(emp["salary"])

# if("department" in emp):
#     print("yes")
# else:
#     print("no")  

stud={"name":"nihala","roll":7,"course":"python"}
# print(stud)

# for k in stud:
    # print(k,stud[k])  

# if("roll" in stud):
#     print("irukk")

# stud["batch"]="may"
# print(stud)

# text="ABABC"

# wc={}

# for l in text:
#     if l in wc:
#         wc[l]+=1
# print(l,"is first recursive character")          #****
#     break
# else:
# wc[l]=1
# print(wc)


# words=["hello","hai","hello","hai","good","morning","evening"]

# wc={}

# for w in words:
#     if w in wc:
#         wc[w]+=1
#     else:
#         wc[w]=1
# print(wc)

# stud={"roll":1234,"name":"hari","age":25,"course":"MCA"}
# # print(stud.items())
# print(stud.get("name"))

# data={
#     "django":"framework",
#      "react":"library",
#      "fastapi":"framework",
#      "ajax":"framework",
#      "uue":"framework"

# }
# wc={}
# for v in data.values():
#     if v in wc:
#         wc[v]+=1
#     else:
#         wc[v]=1
# print(wc)    

# for ke,val in data.items():
#     if val in wc:
#         wc[val].append(ke)
#     else:
#         wc[val]=[ke]                    #*****  recursive-error plus break part,nd this one
# print(wc)  
# 
# square=lambda n:n**3
# print(square(3))      

# add=lambda n1,n2:n1+n2
# print(add(2,3))

# sub=lambda n1,n2: n2-n1
# print(sub(5,5))

# employee={"id":100,"name":"vijay","department":"hr","salary":25000}
# # print(employee.get("name"))
# def gt_name(emp):
#     return(emp.get("name"))
# # print(gt_name(employee))
# gtt_name=lambda emp:emp.get("name")
# # print(gtt_name(employee))
# getsalary=lambda emp:emp.get("salary")
# print(getsalary(employee))

# def additionn(*args):
#     return sum(args)
# print(additionn(10,10,10))

# addition=lambda *args:sum(args)
# print(addition(4,4))

# max_nums=lambda *args:max(args)
# print(max_nums(8,6,5))

words=["hi","hey","mornin"]
# # print(min(words,key=lambda w:len(w)) )
# print(max(words,key=lambda w:len(w)))

# lst=[1,56,78,2]
# print(sorted(lst,reverse=True))
# ans=sorted(words,reverse=True,key=lambda w:len(w))
# print(ans)

# text="ABBAACD"
# wc={}
# for le in text:
#     if le in wc:
#         wc[le]+=1
#     else:
#         wc[le]=1
# print(max(wc,key=lambda l:wc.get(l)))   #maximum repeated letter A    

# movies={"2018":6,"kerelastory":4,"neymar":5.5,"kgf":8}
# #top rated only
# print(max(movies,key=lambda o:movies.get(o))) 

weather=[
    {"tvm":25},
    {"alpy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22}
    ]
temperatr={}


lst=[1,2,3,4,5]

# squares=[n**2 for n in lst]
# print(squares)

# squares=list(map(lambda n:n**2,lst))
# print(squares)

# cube=list(map(lambda n:n**3,lst))
# print(cube)
#if conditn varuvanel we can use filter  find odds,even,num>3
# odds=list(filter(lambda n:n%2!=0,lst))
# # print(odds)
# evens=list(filter(lambda n:n%2==0,lst))
# # print(evens)

# greater=list(filter(lambda n:n>3,lst))
# print(greater)

items=[
    {"name":"biryani","price":130,"category":"non-veg"},
    {"name":"dosa","price":70,"category":"veg"},
    {"name":"vegfriedrice","price":130,"category":"veg"},
    {"name":"noodles","price":130,"category":"nonveg"},
    {"name":"burger","price":130,"category":"nonveg"}
    ]

item_price=list(map(lambda i:i.get("price"),items))
# print(item_price)

item_name=list(map(lambda i:i.get("name"),items))
# print(item_name)

price=[i.get("price") for i in items]
# print(price)

veg_filter=list(map(lambda i:i.get("category"),items))
print(veg_filter)




