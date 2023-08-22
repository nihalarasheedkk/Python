# 20/6

sen="joel is a very good student in may batch"
# words=sen.split(" ")

# print(sen.startswith("joel"))
# bol=sen.startswith("joel")
# print(bol)


# sen="joel is a very good student in may batch"
# words=sen.split(" ")

# #print(sen.startswith("joel"))
# bol=sen.startswith("joel")
# print(bol)
# if bol==True:
#     print("the sentence is starting with joel")

#import package name
# import re  #regular exprsn
# sen="is a very good student in may batch" #sen=>sentence
# x=re.search("^is",sen) #cap letter
# y=re.search("^joel",sen)
# print(x)
# print(y)
#0/p: (0,4) is position 0 to 4

# n
# print(en)
# print(x)
# print(y)

#space is considered by search

#country code of mobile
# import re
# mob=input("enter ur mobile numbr with country code :")
# x=re.search("^[+]91",mob)

# if(x):
#     print("given number is indian")

# else:
#     print("given number is foreign")
# import re
# resi=input("enter a residence number")
# ekm=re.search("^0484",resi)
# ijk=re.search("^0480",resi)
# tcr=re.search("^0487",resi)
# mpr=re.search("^0494",resi)
# ksd=re.search("^04994",resi)
# cct=re.search("^0495",resi)
# if ekm:
#     print("ernakulam")
# elif ijk:
#     print("irinjalakuda")
# elif tcr:
#     print("tcr")
# elif mpr:
#     print("mpr")
# elif ksd:
#     print("ksd")
# else:
#     print("calicutt")    



#21/06
#verify gmail
# import re
# gmail=input("enter ur email:")
# g=re.search("@gmail.com$",gmail)
# if g:
#     print("it is valid")
# else:
#     print("not valid")   


#{} => used to check whether repeating
 
# import re 
# text="abababab"
# text1="aaaabbbbbccc"
# t=re.search("[a]{4}",text)
# t1=re.search("[a]{4}",text1)
# print(t)
# print(t1) 
#abcd56789
# te="abcd1234"
# check=re.search("[a-z]{4}",te) 
# print(check) 

#hw: mobile number verificatn +91[10positions -digits]

#cap letters also include

# stri="3457abDARG5643"
# s=re.search("[a-z]{2}[A-Z]{4}",stri)
# print(s)

#re.sub function

# import re
# stri="hello how r u"
# s=re.sub(" ","," ,stri)
# print(s)

# import re
# re.py
#search()
#sub()
#fullmatch()
#findall()



# import re
# mob=input("enter your mob num with country code:")
# print(mob)
# x=re.search("^91",mob)
# if(x):
#     print("num is indian")
# else:
#     print("num is not indian")

#* * * * *
# from re import*

# text="luminar techno lab luminar techno hub"
# matcher=finditer("luminar",text)

# count=0
# for m in matcher:
#     count+=1
# print(count)  
  
# import re
# text="aabdXYZ$#098"

# matcher=re.finditer("[^a-zA-Z0-9]",text)
# print(matcher)
# for m in matcher:
#     print(m.group())

# var_name="k6123"

# rule="[k-m][369][a-zA-Z0-9]*"

# from re import *

# rule="[k-m][369][a-zA-Z0-9]*"  #astrics given to these rules can ethra thavana venelum vara

# var_name="k3llo"

# matcher=fullmatch(rule,var_name)
# if matcher!=None:
#     print("valid")
# else:
#     print("invalid") 


# from re import *
# rule="[a-zA-Z_][a-zA-Z0-9_]*"
# var_name="num#"  

# matcher=fullmatch(rule,var_name)
# if matcher==None:
#     print("invalid")
# else:
#     print("valid")   

# from re import*
# rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{4}"
# veh_num="TN-08-av-2794"

# matcher=fullmatch(rule,veh_num)
# print("invalid" if matcher==None else "valid")

#valid kerela vehicle numbs
violations=["kl-08-av-2794",
            "kl-08-av-4970",
            "kl-01-av-14",
            "kl-01-av-1",
            "kl-01-av-12",
            "TN-01-av-1",
            "ghz-01-avo-1",
            "0kl-01-av-10"
]

# rule="[K][L][-][0-9]{2}[-][a-z]{2}[-][0-9]{1,4}"
# for num in violations:
 
#  matcher=fullmatch(rule,num)
# if matcher!=None:
#   print(num)

