from json import load

with open("C:\\Users\\user\\OneDrive\\Desktop\\mypythonprograms\\leapyear\\jasonprocess\\jsonprocess\\data.json","r") as f:
    data=load(f) #to read to dat

# names=[u.get("name") for u in data]  #list comp back agaain
 
# print(names)

#student with highest marh
# lst=[10,30,40]

# candidate=max(data,key=lambda s:s.get("total"))
# print(candidate)

#sort all students total in desc order
# out=sorted(data,reverse=True,key=lambda s:s.get("total")) #total is the keyword given in data.json
# print(out)

bca_stud=[u.get("name") for u in data if u.get("course")=="bca"]
print(bca_stud)