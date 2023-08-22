# square=lambda n:n**3
# print(square(3))

# add=lambda n1,n2:n1+n2
# print(add(5,15))

# sub= lambda n1,n2: n2-n1
# print(sub(5,5))

#f/n to lambda

# employee={"id":100,"name":"vijay","department":"hr","salary":25000}
# print(employee.get("name"))

    #f/n
# def get_name(emp):
#     return(emp.get("name"))
# print(get_name(employee))

# get_name=lambda emp:emp.get("name")
# print(get_name(employee))

#return salary=>
# get_salary=lambda emp:emp.get("salary")
# print(get_salary(employee))

#     * astrics args positional argument takes any number of parameters type tuple
# def addition(*args):
#     return sum(args)

# print(addition(10,10,10))

# addition=lambda *args:sum(args)
# print(addition(3,4))

#to find max numbs:
# max_nums=lambda *args:max(args)
# print(max_nums(10,5))

# max_nums=lambda *args:max(args)
# print(max_nums(8,3,1))

# words=["hello","hi","goood morning"]

# print(min(words,key=lambda w:len(w)))

# print(max(words,key=lambda w:len(w)))

# lst=[1,56,78,2]
# # print(sorted(lst))

# #descending order
# # print(sorted(lst,reverse=True))
#    ****
# words=["in","hello","hai","pneopppen","good"]

# out=sorted(words,reverse=True,key=lambda w:len(w))
# print(out)

# text="ABBAACD"
# #most recursive character
# wc={}
# for ch in text:
#     if ch in wc:
#         wc[ch]+=1
#     else:
#         wc[ch]=1

  #1,1,1,1,2,2,3,5,6,8,8      
# print(min(wc,key=lambda k:wc.get(k)))

#max
# print(max(wc,key=lambda k:wc.get(k)))

movies={"2018":5,"kerelastory":3,"neymar":4,"kgf":5,"arm":4}

#print all movie names

# print(movies.keys())

#print top rated movies
# print(max(movies,key=lambda k:movies.get(k)))                   #keys()--movie names return
#keys()--movie names return
#values()--
 #items()--

 #sort movies wrt rating order by desc
# out=sorted(movies,reverse=True,key=lambda k:movies.get(k))
# print(out)


# mobiles=[
# {"name":"galaxy10","brand":"samsung","price":24000,"network":"4g","colour":["black","grey"]},
# {"name":"nokia7.1","brand":"nokia","price":18000,"network":"4g","colour":["silver","gold"]},
# {"name":"iphone11","brand":"apple","price":90000,"network":"5g","colour":["white","blue"]}
# ]

#list of dictionary

#             *******
weather=[
    {"tvm":25},
    {"apy":23},
    {"kty":27},
    {"idk":18},
    {"ekm":29},
    {"tsr":28},
    {"tvm":26},
    {"apy":22},
    {"kty":28},
    {"idk":19},
    {"ekm":30},
    {"tsr":22},
]

temp={}
for t in weather:
    for k,v in t.items():
     district_name=k
    current_temp=v

    if district_name in temp:
            #pass
            old_temp=temp[district_name]
    if current_temp>old_temp:
                
                temp[district_name]=current_temp

    else:
                temp[district_name]=current_temp
print(temp)  

#for max        hw
# for t in weather:
    for k,v in t.items():
        district_name=k
        temp=v
        if 

        










    

                                                                
                                                               
                                                
                                                                











    
