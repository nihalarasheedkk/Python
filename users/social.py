f=open("C:\Users\user\OneDrive\Desktop\mypythonprograms\users\data.txt","r")

users=[]
for line in f:
    text=line.rstrip("\n")
    name,followers,followings=text.split(",")
print(name,followers,followings)

