# expenses=[20000,23000,15000,14000,35000]
# for exp in expenses:
#     print(exp)
# for exp in expenses:
#     if exp>16000:
# print(exp)
        #to print the maximum number
        #max()  built in function  min() sum()
# max_exp=max(expenses)
# print(max_exp)
# min_exp=min(expenses)
# print(min_exp)

# total=sum(expenses)
# print(total)

# arr=[2,3,4]
# op=[]
# total=sum(arr)
# print(total)

# for num in arr:
#     number=total-num
  
#     op.append(number)
# print(op)


# numbers=[2,7,8,9,12,13]
# odds=[]
# evens=[]
# for num in numbers:
#     if num%2==0:
#         evens.append(num)
    
#     else:
#         odds.append(num)
# print(evens)
# print(odds)

users=["sachin","kohli","sehwag","rahul","dhoni","raina"]
sachin_followers=["kohli","sehwag","rahul"]

name=[]
for suggestion in users:
    if suggestion not in sachin_followers:
        name.append(suggestion)
print(name)


