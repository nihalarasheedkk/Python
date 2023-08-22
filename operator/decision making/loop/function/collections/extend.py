#extend:

# food1=["rice","egg","fried rice"]
# food2=["noodle","fish"]
# food1.extend(food2)
# print(food1)

#remove:
# to remove elements
#listname.remove(the value to be removed)

# number=[1,2,3]
# number.remove(3)
# print(number)

# fruits=["apple","mango","orange"]
# fruits.remove("apple")
# print(fruits)
# fruits.remove(fruits[0])
# print(fruits)

#pop:
# bikes=["splender","interceptor","jawa","ducatti920"]
# b=bikes.pop()
# print(b)
# print(bikes)

# b1=bikes.pop(2) #position
# print(b1)
# print(bikes)

#delete and clear

#del:
# del listname
# bikes=["splender","interceptor","jawa","ducatti920"]
# del bikes
# print(bikes)

#clear
#listname.clear()
# bikes.clear()
# print(bikes)

#friday
# bird=["peacock","pigeon","duck","hen"]
# check_bird=input('enter a bird:')
# for i in bird:
#     if i==check_bird:
#         bird.remove(i)
# print(bird)   

#last in first out    STACK
# list=[]
# list.append(10)
# list.append(20)
# list.append(30)        #3 values 3 times pop cheyya
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)
# list.pop()
# print(list)

#QUEUE
#queue.append()
# queue=[]
# queue.append(10)
# queue.append(20)
# queue.append(30)
# print(queue)

# queue.pop(0)
# print(queue)
# queue.pop(1)
# print(queue)

#membership operator     only available in python   not in also
# lst=[12,13,14,15,16]
# x=20
# if x in lst:
#     print("is there")
# else:
#     print("not there")

# if x not in lst:
#     print("is not there")

# cars=["lamborgini","maruthi800","porshe","bmw"]
# car_o=[]
# for c in cars:
#     if "o" in c:
#         car_o.append(c)
# print(car_o)

#remove first 3rd and 4th elements frm a list
#    0 1 2 3  4
# lst=[2,5,7,10,15]
# lst.pop(0)
# print(lst)
# lst.pop(2-1)
# print(lst)
# lst.pop(3-2)
# print(lst)

#create a nw list frm a given list of integers
#create a nw list frm this list(but should be odd and multiples of 5)

# list=[10,15,20,25,30]
# new_list=[]
# for num in list:
#     if num%2!=0:
#         if num%5==0:
#             new_list.append(num)
# print(new_list)

#find greatest value frm the given list vthout usin max()
lst=[2,6,10]
maximum=lst[0]
for num in lst:
    if maximum<num:
        maximum=num

print("greatest number in list:",maximum)    #video








