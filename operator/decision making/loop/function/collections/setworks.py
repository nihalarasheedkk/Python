# st={10,20,"hello","hai",True}
# # for elem in st:
# #     print(elem)

# st.add(100)
# print(st)

# #changing list to set
# lst=[1,2,3,4,5,6]
# st=set(lst)
# print(st)

# st1={10,11,12,13}
# st2={10,12,25,30}

                #union()
# union_set=st1.union(st2)
# print(union_set)

                     #intersection()
# intersection_set=st1.intersection(st2)
# print(intersection_set)

                   #difference()
# difference_set=st1.difference(st2)
# print(difference_set)

# lst=[10,20,10,20,12,13,14]
# st=set(lst)
# print(st)

# allusers=["mohanlal","fahad","dq","vijay","nivin","asif"]

# dq_friendlist=["mohanlal","fahad","asif"]
# asif_friendlist=["mohanlal","fahad","vijay","nivin"]

# suggestions=set(allusers).difference(set(dq_friendlist))
# suggestions.remove("dq")
# print(suggestions)

#dq=>asif  mutual friends

# mutual_friends=set(dq_friendlist).intersection(set(asif_friendlist))
# print(mutual_friends)

word="pneumonoultramicroscopicsilicovolcanoconiosis"
#print number of vowels
for ch in word:
    print(ch)

    vowels={"a","e","i","o"}
    