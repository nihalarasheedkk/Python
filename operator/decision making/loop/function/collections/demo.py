"""
#function     #builtins.py contains utility function and classes
Def Print()
Def Input()
Def Type()
Def Max()
Def Min()
Def Sum()
sorted()
"""
#if theres a dot its a class under list
#.append

#classes
"""
#list    methods:
append()
clear()
copy()
count()
index()
reverse()
sort()
remove()
pop()
extend()
insert()
"""
#to know the classes and attributes : print(dir(set))

# lst=[2,3,4,5]
# sum=7

# for i in lst:
#     for j in lst:
#         if(i !=j and i<j):
#             cur_sum=i+j    #operation
#             if(cur_sum==sum):
#              print(i,j)
             
# lst=[2,3,4,5]
# sum=8

# low=0
# upp=len(lst)-1

# while(low<upp): #condition
#     cur_sum=lst[low]+lst[upp]  #position lst[]
#     if(cur_sum==sum):
#         print("pairs",lst[low],lst[upp])
#         low+=1
#         #break

#     elif(cur_sum<sum):
#         low+=1
#     elif(cur_sum>sum):
#         upp-=1  

# lst1=[10,14,15,20,21]
# lst2=[8,9,20,21,22]

# for n1 in lst1:
#     for n2 in lst2:
#         if(n1==n2):
#             print(n1)

# lst=[1,2,3,4]
# elem=20
# if elem in lst:
#     print("element found")
# else:
#     print("element not found")

          # ****

# lst1=[10,14,15,20,21]
# lst2=[8,9,20,21,22]
# (p1,p2)=(0,0)

# while(p1<len(lst1) and p2<len(lst2)):
#     if(lst1[p1]==lst2[p2]):
#         print(lst1[p1], "same pair")
#         p1+=1 #move p1
#     elif(lst1[p1] < lst2[p2]):
#         p1+=1  
#     elif(lst1[p1] > lst2[p2]):
#         p2+=1    


#lst=[1,3,4,6]
#find least +ve missing integer frm given list
# lst=[1,3,4,6]          #p2 - p1 = 1 consecutive     != 1 not consecutive  3-1=2 vch is not 1 so not cons
# for i in range(0,len(lst)):
#     elem1=lst[i]            #i=0
#     elem2=lst[i+1]    #num nxt to 

#     if elem2-elem1 !=1:
#         print(elem1+1,  "is missing")
#         break

# lst=[1,2,4,5,8]

# for i in range(0,len(lst)):
#     if lst[0]!=1:
#         print(1,"is missing")
#         break
#     else:
#         elem1=lst[i]
#         elem2=lst[i+1]
#         if elem2-elem1 !=1:
#             print(elem1+1,"is missing")
#             break

#without usin 'in' check elem in the list

# lst=[2,3,4,5,6,7,8]

# element=6
# is_found=False

# for i in range(0,len(lst)):
#     if element==lst[i]:
#         is_found=True
#         break
# print("found" if is_found==True else "not found")    