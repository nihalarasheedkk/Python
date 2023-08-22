#dictionary
#{key:value,key:value}
#key is unique

emp={"id":100,"name":"hari","desig":"HR","salary":250000}
# print(emp)

# #print emp name
# print(emp["name"])

# #print emp salary
# print(emp["salary"])

#ITERATE DICTIONARY
# for key in emp:
#     print(key,emp[key])

#addding new key-value pair:
#dictname["nw key"]="nw value"

# emp["gender"]="male"
# print(emp)

#updating value
# emp["salary"]=27000
# print(emp)


# #update employee salary with current salary +2000
# emp["salary"]+=2000
# print(emp["salary"])  #to print salary alone

#check existance of a key
# if("name" in emp):
#     print("present")
# else:
#     print("not present")

# stud={"name":"nih","roll":7,"course":"python"}
# print(stud)

# for key in stud:
#     print(key,stud[key])

# if("roll" in stud):
#     print("irukk")

# stud["batch"]="may"
# print(stud)            #to give discount mob["price"]-=500

# text="ABABC"
# #find first recursive character(repeated character)  a two time  b two  c one
# Wc={}  #empty bracket  #A:1  key:value
# for ch in text:
#     if ch in Wc:   #ch=A
#         Wc[ch]+=1
#         # print(ch, "is first recursive character")
#         # break
#     else:
#         Wc[ch]=1
# print(Wc)

#hw words=["hello","hai","hello","hai","good","morning","evening"]    #word count
#estimated o/p   hello:2 hai:2 
                #****

# words=["hello","hai","hello","hai","good","morning","evening"]
# wc={}
# #word count
# for word in words:
#     if word in wc:
#         wc[word]+=1

#     else:
#         wc[word]=1

# print(wc)


#list(append,pop,insert,extend,)
#set()
#tuple()
#dict()

#methods:

#values()

student={"roll":1234,"name":"hari","age":25,"course":"MCA"}
# #to take values outta dictionary use .values()
# print(student.values())

#keys()
# print(student.keys())

#items()
# print(student.items())

# for k,v in student.items():
#     print(k,v)

#get(key) fetching value wth key           *invalid key kodutha 'none' enn print avum nd execution stops

# print(student.get("names"))
# print("file transfer")
# print("database commit")

#pop(key) : pass the (key) to pop/remove
# student.pop("course")
# print(student)

#dictionary count
# data={
#      "django":"framework",
#     "react":"library",
#     "fastapi":"framework",
#     "vue":"framework",
#     "ajax":"library"
#     }

# wc={}
# for values in data.values():
#     if values in wc:
#         wc[values]+=1

#     else:
#         wc[values]=1

# print(wc)

#estimated op=> {'framework': ['django', 'fastapi', 'vue'], 'library': ['react', 'ajax']}

#key n values needed so use items()
# for key,value in data.items():
#     if value in wc:  #box
#         wc[value].append(key)

#     else:
#         wc[value]=[key]
# print(wc)        


"""
# text="AABBCCCDE"
# print most recursive character in given text

# q2
text="goodmorning hello goodevening hello"
# print longest word in given text
"""
text="AABBCCCDE"
# print most recursive character in given text

# q2
# text="goodmorning hello goodevening hello"
# print longest word in given text
wc={}
for ch in text:
    if ch in wc:
        wc[ch]+=1
print(wc)


    









