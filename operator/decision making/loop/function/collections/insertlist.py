# lst=[2,3,4,5]
# # lst.append(6)
# # print(lst)


# #insert()  to add values to a particular position
# lst.insert(0,1)  #(position,value to add)
# print(lst)

# emptylist=[]
# print(emptylist)
# length=int(input("Enter size of the list :"))
# for i in range(length):
#     num=int(input(f"enter the {i}th position element"))
#     # num=int(input(i))    
#     emptylist.append(num)
# print(emptylist)

# emptylist=[]
# length=int(input("enter a number")) #to type length
# for i in range(length):
#     num=int(input(f"enter the {i}the position of the elem")) 
#  #add nw eleme to 2nd posit of list vch shud be max of list ,add vth 10
# emptylist.append(num)


# max_length=max(emptylist)
# emptylist.insert(2,max_length+10)
# print(emptylist)

"""create a list of student names then check for a particular name in the list given by the user if name is 
present then change that name to anamika, if that partic.. name is not present add 'amal' to the first
position of the list"""

# students=["anu","manu","priya","nila"]
# names=input("enter a name")                   #withpout user

# for s in students:
#     if s==names:
#         print("anamika")
# else:
#     students.insert(0,"amal")
# print(students)

#hw: if duplicate values r present how the values will be cahnged if a match is found or not
#input=[a,b,c,a]  check name a
#output=[anamika,b,c,anamika]
stud_name=[]
length=int(input("enter the size"))
for i in range(length): #i=0 0<3, i=1....
    name=input(f"enter the {i}the name:")
    stud_name.append(name) #stud_name=[a]  stud_name=[a,b]...

check_name=input("enter first name:") #check_name=d


for i in range(len(stud_name)):
    if(check_name==stud_name[i]):
        stud_name[i]="anamika"
        rep=2
        if(rep==0):
            stud_name.insert(1,"amal")
            print(stud_name)
#ask

